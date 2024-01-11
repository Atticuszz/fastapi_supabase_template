from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud import item
from app.schemas import Item, ItemCreate, ItemUpdate

router = APIRouter()


@router.post("/create-item", response_model=Item)
async def create_item(item_in: ItemCreate, session: SessionDep) -> Item:
    return await item.create(session, obj_in=item_in)


@router.get("/read-item", response_model=list[Item])
async def read_items(session: SessionDep) -> list[Item]:
    return await item.get_multi_by_table_name(session)


@router.put("/update-item", response_model=Item)
async def update_item(item_in: ItemUpdate, session: SessionDep) -> Item:
    return await item.update(session, obj_in=item_in)


@router.delete("/delete", response_model=Item)
async def delete_item(item_in: ItemUpdate, session: SessionDep) -> Item:
    return await item.delete(session, obj_in=item_in)
