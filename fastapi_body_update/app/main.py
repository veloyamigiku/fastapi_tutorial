from datetime import datetime
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from typing import Union

app = FastAPI()

@app.get('/health_check')
async def check_health():
    return {
        'health_check': 'ok'
    }

class Item(BaseModel):
    name: Union[str, None] = None
    description: Union[str, None] = None
    price: Union[float, None] = None
    tax: float = 10.5
    tags: list[str] = []

items = {
    'foo': {
        'name': 'Foo',
        'price': 50.2
    },
    'bar': {
        'name': 'Bar',
        'description': 'The bartenders',
        'price': 62,
        'tax': 20.2
    },
    'baz': {
        'name': 'Baz',
        'description': None,
        'price': 50.2,
        'tax': 10.5,
        'tags': []
    }
}

@app.get(
    '/items/{item_id}',
    response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

@app.put(
    '/items/{item_id}',
    response_model=Item)
async def put_item(
    item_id: str,
    item: Item):

    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded

@app.patch(
    '/items/{item_id}',
    response_model=Item)
async def patch_item(
    item_id: str,
    item: Item):
    stored_item_data = items[item_id]
    stored_item_model = Item(**stored_item_data)
    update_data = item.dict(exclude_unset=True)
    updated_item = stored_item_model.copy(update=update_data)
    items[item_id] = jsonable_encoder(updated_item)
    return updated_item
