# coding=utf-8
import asyncio
import os

from dotenv import load_dotenv
from postgrest import APIResponse

from src.fastapi_app.dependencies.decorator import retry
from supabase_py_async import create_client, AsyncClient
from supabase_py_async.lib.client_options import ClientOptions

load_dotenv()


class SupaBase:
    def __init__(self, url: str = os.getenv("SUPABASE_URL"),
                 key: str = os.getenv("SUPABASE_KEY")):
        self.client: AsyncClient = create_client(
            url, key, options=ClientOptions(
                postgrest_client_timeout=10, storage_client_timeout=10))

    @retry
    async def get_table(self, name: str, columns: list[str] | None = None) -> list[dict]:
        if columns is None:
            columns = ["*"]
        select_params: str = ",".join(columns)
        response: APIResponse = await self.client.table(name).select(select_params).execute()
        return response.data

    @retry
    async def upsert(self, name: str, data: dict) -> list[dict]:
        response: APIResponse = await self.client.table(name).upsert(data).execute()
        return response.data

    @retry
    async def delete(self, name: str, uuid: str) -> list[dict]:
        response: APIResponse = await self.client.table(
            name).delete().eq("uuid", uuid).execute()
        return response.data

    async def multi_requests(self, name: str, data: list[dict], options: str, chunk_size: int = 4000):

        for i in range(0, len(data), chunk_size):
            chunk_data = data[i:i + chunk_size]
            match options:
                case "upsert":
                    tasks = [asyncio.ensure_future(self.upsert(name, item))
                             for item in chunk_data]
                case 'delete':
                    tasks = [
                        asyncio.ensure_future(
                            self.delete(name,
                                        item["uuid"])) for item in chunk_data]
                case _:
                    raise ValueError("options must be 'upsert' or 'delete'")
            await asyncio.gather(*tasks)
        return


supabase_client = SupaBase()


async def main():
    data = await supabase_client.get_table("task_done_list")
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
    # 将数据转换为json数据
