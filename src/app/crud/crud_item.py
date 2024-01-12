from supabase_py_async import AsyncClient

from app.crud.base import CRUDBase
from app.schemas import Item, ItemCreate, ItemUpdate


class CRUDItem(CRUDBase[Item, ItemCreate, ItemUpdate]):
    async def create(self, db: AsyncClient, *, obj_in: ItemCreate) -> Item:
        return await super().create(db, obj_in=obj_in)

    async def get(self, db: AsyncClient, *, id: str) -> Item | None:
        return await super().get(db, id=id)

    async def get_all(self, db: AsyncClient) -> list[Item]:
        return await super().get_all(db)

    async def get_multi_by_owner(self, db: AsyncClient) -> list[Item]:
        return await super().get_multi_by_owner(db)

    async def update(self, db: AsyncClient, *, obj_in: ItemUpdate) -> Item:
        return await super().update(db, obj_in=obj_in)

    async def delete(self, db: AsyncClient, *, obj_in: ItemUpdate) -> Item:
        return await super().delete(db, obj_in=obj_in)


item = CRUDItem(Item)
