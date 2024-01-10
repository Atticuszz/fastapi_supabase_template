from typing import Generic, TypeVar

from pydantic import BaseModel
from supabase_py_async import AsyncClient

ModelType = TypeVar("ModelType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: type[ModelType]):
        self.model = model

    async def get(self, db: AsyncClient, *, table_name: str, id: str) -> ModelType | None:
        """get by table_name"""

    async def create(
            self, db: AsyncClient, *, obj_in: CreateSchemaType
    ) -> ModelType | None:
        """create by CreateSchemaType"""

    async def update(
            self, db: AsyncClient, *, obj_in: UpdateSchemaType
    ) -> ModelType | None:
        """update by UpdateSchemaType"""

    async def delete(
            self, db: AsyncClient, *, obj_in: UpdateSchemaType
    ) -> ModelType | None:
        """remove by UpdateSchemaType"""
