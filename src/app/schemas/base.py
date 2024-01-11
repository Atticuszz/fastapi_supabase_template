"""
-*- coding: utf-8 -*-
@Organization : SupaVision
@Author       : 18317
@Date Created : 11/01/2024
@Description  :
"""
from pydantic import BaseModel, Extra

## request


# Shared properties
# class CRUDBaseModel(BaseModel):
#     # where the data
#     table_name: str


# Properties to receive on item creation
# in
class CreateBase(BaseModel):
    # inherent to add more properties for creating
    pass


# Properties to receive on item update
# in


class UpdateBase(BaseModel):
    # inherent to add more properties for updating
    id: str


## response


# Properties shared by models stored in DB
class InDBBase(BaseModel):
    id: str
    user_id: str
    created_at: str


# Properties to return to client
# curd model
# out
class ResponseBase(InDBBase):
    # inherent to add more properties for responding
    @property
    def table_name(self) -> str:
        return self.__class__.__name__.lower()

    class Config:
        extra = Extra.ignore
