import pytest
from faker import Faker
from supabase._async.client import AsyncClient

from app import crud
from app.schemas.item import Item, ItemCreate, ItemUpdate


@pytest.mark.anyio
async def test_create_item(db: AsyncClient) -> None:
    test_data = Faker().text()
    item_in = ItemCreate(test_data=test_data)
    item: Item = await crud.item.create(db=db, obj_in=item_in)
    assert item.test_data == test_data


@pytest.mark.anyio
async def test_get_item(db: AsyncClient) -> None:
    test_data = Faker().text()
    item_in = ItemCreate(table_name="test_table", test_data=test_data)
    item: Item = await crud.item.create(db=db, obj_in=item_in)
    stored_item = await crud.item.get(db, id=item.id)
    assert stored_item
    assert item.id == stored_item.id
    assert item.test_data == stored_item.test_data


@pytest.mark.anyio
async def test_update_item(db: AsyncClient) -> None:
    test_data = Faker().text()
    item_in = ItemCreate(table_name="test_table", test_data=test_data)
    item: Item = await crud.item.create(db=db, obj_in=item_in)
    test_data2 = Faker().text()
    item_update = ItemUpdate(table_name="test_table", id=item.id, test_data=test_data2)
    item2 = await crud.item.update(db=db, obj_in=item_update)
    assert item.id == item2.id
    assert item.test_data != item2.test_data
    assert item2.test_data == test_data2


@pytest.mark.anyio
async def test_delete_item(db: AsyncClient) -> None:
    test_data = Faker().text()
    item_in = ItemCreate(table_name="test_table", test_data=test_data)
    item: Item = await crud.item.create(db=db, obj_in=item_in)
    item2 = await crud.item.delete(db=db, id=item.id)
    item3 = await crud.item.get(db, id=item.id)
    assert item3 is None
    assert item.id == item2.id
    assert item.test_data == item2.test_data
    assert item2.test_data == test_data
