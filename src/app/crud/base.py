import logging
from typing import Generic, TypeVar

from supabase_py_async import AsyncClient

from app.schemas.base import CreateBase, ResponseBase, UpdateBase

ModelType = TypeVar("ModelType", bound=ResponseBase)
CreateSchemaType = TypeVar("CreateSchemaType", bound=CreateBase)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=UpdateBase)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    async def get(self, db: AsyncClient, *, id: str) -> ModelType:
        """get by table_name"""
        data, count = (
            await db.table(self.model.table_name).select("*").eq("id", id).execute()
        )
        return self.model(**data[0])

    async def create(self, db: AsyncClient, *, obj_in: CreateSchemaType) -> ModelType:
        """create by CreateSchemaType"""
        # FIXME: create with wrong url
        logging.info(obj_in.model_dump())
        data, count = (
            await db.table(self.model.table_name).insert(obj_in.model_dump()).execute()
        )
        return self.model(**data[0])

    async def update(self, db: AsyncClient, *, obj_in: UpdateSchemaType) -> ModelType:
        """update by UpdateSchemaType"""
        data, count = (
            await db.table(self.model.table_name)
            .update(obj_in.model_dump())
            .eq("id", obj_in.id)
            .execute()
        )
        return self.model(**data[0])

    async def delete(self, db: AsyncClient, *, obj_in: UpdateSchemaType) -> ModelType:
        """remove by UpdateSchemaType"""
        data, count = (
            await db.table(self.model.table_name).delete().eq("id", obj_in.id).execute()
        )
        return self.model(**data[0])
