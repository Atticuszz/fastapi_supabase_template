from typing import Any, Generic, TypeVar

from pydantic import BaseModel
from supabase_py_async import AsyncClient

ModelType = TypeVar("ModelType", bound=Any)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):

    def get(self, db: AsyncClient, id: str) -> ModelType | None:
        pass

    def create(self, db: AsyncClient, *, obj_in: CreateSchemaType) -> ModelType:
        pass

    def update(self, db: AsyncClient, *, obj_in: CreateSchemaType) -> ModelType:
        pass

    def remove(self, db: AsyncClient, *, id: str) -> ModelType:
        pass
