from fastapi import APIRouter
from src.api.deps import SessionDep
from src.schemas import ItemCreate, ItemUpdate, Item
from src.crud import item

router = APIRouter()


@router.post("/create-item", response_model=Item)
async def create_item(item_in: ItemCreate, db: SessionDep):
    return await item.create(db=db, obj_in=item_in)


@router.get("/read-item", response_model=list[Item])
async def read_items(db: SessionDep):
    return await item.get_multi_by_table_name(db=db, table_name="items")


@router.put("/update-item/{id}", response_model=Item)
async def update_item(id: str, item_in: ItemUpdate, db: SessionDep):
    return await item.update(db=db, obj_in=item_in)


@router.delete("/delete/{id}", response_model=Item)
async def delete_item(id: str, db: SessionDep):
    return await item.delete(db=db, id=id)
