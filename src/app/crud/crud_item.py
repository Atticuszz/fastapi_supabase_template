from supabase_py_async import AsyncClient

from app.crud.base import CRUDBase
from app.schemas import Item, ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    async def create(self, db: AsyncClient, *, obj_in: ItemCreate) -> Item:
        return await super().create(db, obj_in=obj_in)

    async def get(self, db: AsyncClient, *, id: str) -> Item:
        return await super().get(db, id=id)

    async def get_multi_by_owner(self, db: AsyncClient) -> list[Item]:
        user_rps = await db.auth.get_user()
        user_id = user_rps.user.id
        data, count = (
            await db.table(self.model.table_name)
            .select("*")
            .eq("user_id", user_id)
            .execute()
        )
        return [self.model(**item) for item in data]

    async def get_multi_by_table_name(self, db: AsyncClient) -> list[Item]:
        data, count = await db.table(self.model.table_name).select("*").execute()
        return [self.model(**item) for item in data]

    async def update(self, db: AsyncClient, *, obj_in: ItemUpdate) -> Item:
        return await super().update(db, obj_in=obj_in)

    async def delete(self, db: AsyncClient, *, obj_in: ItemUpdate) -> Item:
        return await super().delete(db, obj_in=obj_in)


item = CRUDItem(Item)
