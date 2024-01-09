from typing import List, Union, Dict, Any
from supabase_py_async import AsyncClient

from src.crud.base import CRUDBase
from src.schemas import ItemCreate, ItemUpdate, Item


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    async def create(
            self, db: AsyncClient, *, obj_in: ItemCreate
    ) -> Item:
        data, count = await db.table(obj_in.table_name).insert(**obj_in.model_dump()).execute()
        return Item(**data[0])

    async def get_multi_by_owner(
            self, db: AsyncClient, *, table_name: str
    ) -> list[Item]:
        user_rps = await db.auth.get_user()
        user_id = user_rps.user.id
        data, count = await db.table(table_name).select("*").eq("user_id", user_id).execute()
        return [Item(**item) for item in data]

    async def get_multi_by_table_name(
            self, db: AsyncClient, table_name: str
    ) -> list[Item]:
        data, count = await db.table(table_name).select("*").execute()
        return [Item(**item) for item in data]

    async def update(self, db: AsyncClient, *, obj_in: ItemUpdate) -> Item:
        data, count = await db.table(ItemUpdate.table_name).update(**obj_in.model_dump()).eq("id", obj_in.id).execute()
        return Item(**data[0])

    async def delete(self, db: AsyncClient, *, id: str) -> Item:
        data, count = await db.table(ItemUpdate.table_name).delete().eq("id", id).execute()
        return Item(**data[0])


item = CRUDItem()
