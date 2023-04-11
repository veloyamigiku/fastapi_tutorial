from enum import Enum
from fastapi import FastAPI
from fastapi import status
from pydantic import BaseModel
from typing import Union

app = FastAPI()

@app.get('/health_check')
async def check_health():
    return {
        'health_check': 'ok'
    }

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    tags: set[str] = set()

class Tags(Enum):
    items = 'items'
    users = 'users'

@app.post(
    '/items/',
    response_model=Item,
    status_code=status.HTTP_201_CREATED,
    tags=[Tags.items],
    summary='Create an item',
    response_description='The created item')#,
    #description='Create an item with all the information, name, description, price, tax and a set of unique tags')
async def create_item(item: Item):
    """
    Create an item with all the information:

    - **name**: each item must have a name
    - **description**: a long description
    - **price**: required
    - **tax**: if the item doesn't have tax, you can omit this
    - **tags**: a set of unique tag string for this item
    """
    return item

@app.get(
    '/items/',
    tags=[Tags.items])
async def read_items():
    return [
        {
            'name': 'Foo',
            'price': 42
        }
    ]

@app.get(
    '/users/',
    tags=[Tags.users])
async def read_users():
    return [
        {
            'username': 'johndoe'
        }
    ]

@app.get(
    '/elements/',
    tags=[Tags.items],
    deprecated=True)
async def read_elements():
    return [
        {
            'item_id': 'Foo'
        }
    ]
