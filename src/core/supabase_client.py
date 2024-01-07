# coding=utf-8
"""
auth and curd supabase
"""
import asyncio
import os

from gotrue import AuthResponse
from postgrest import APIResponse

from supabase_py_async import AsyncClient, create_client
from supabase_py_async.lib.client_options import ClientOptions
from ..common import retry


class ClientBase:
    def __init__(self):
        self.client: AsyncClient | None = None

    async def init_supabse():
        url: str = os.getenv("SUPABASE_URL")
        key: str = os.getenv("SUPABASE_KEY")
        supabase_client.client = await create_client(url, key, options=ClientOptions(
            postgrest_client_timeout=10, storage_client_timeout=10))
        assert supabase_client.client is not None

# TODO: separate supabase into several types curd class
class SupaBase(ClientBase):

    async def set_session(self, access_token: str, refresh_token: str) -> AuthResponse:
        """
        set session for continue curd supabase
        :exception AuthSessionMissingError: Could not set session
        """
        response: AuthResponse = await self.client.auth.set_session(access_token=access_token,
                                                                    refresh_token=refresh_token)
        return response

    async def refresh_session(self, refresh_token: str) -> AuthResponse:
        """
        refresh token for front end
        :exception AuthApiError: Could not refresh token
        """
        new_session: AuthResponse = await self.client.auth.refresh_session(refresh_token)

        return new_session

    async def sign_in(self, email: str, password: str) -> AuthResponse:
        """
        sign in with email and password
        :exception AuthApiError: Invalid email or password
        """
        response: AuthResponse = await self.client.auth.sign_in_with_password(
            {'email': email, 'password': password})

        return response

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


# TODO:

async def main():
    import os
    from dotenv import load_dotenv
    load_dotenv()
    url: str = os.getenv("SUPABASE_URL")
    key: str = os.getenv("SUPABASE_KEY")
    supabase_client.client = await create_client(url, key, options=ClientOptions(
        postgrest_client_timeout=10, storage_client_timeout=10))
    data = await supabase_client.get_table("task_done_list")
    print(data)


if __name__ == "__main__":
    asyncio.run(main())
    # 将数据转换为json数据
