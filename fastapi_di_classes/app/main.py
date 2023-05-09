from fastapi import Depends
from fastapi import FastAPI
from typing import Annotated
from typing import Any
from typing import Union

app = FastAPI()

@app.get('/health_check')
async def check_health():
    return {
        'health_check': 'ok'
    }

fake_items_db = [
    {
        'item_name': 'Foo'
    },
    {
        'item_name': 'Bar'
    },
    {
        'item_name': 'Baz'
    }
]

class CommonQueryParams:
    def __init__(
        self,
        q: Union[str, None] = None,
        skip: int = 0,
        limit: int = 100) -> None:
        self.q = q
        self.skip = skip
        self.limit = limit        

@app.get('/items/')
async def read_item(commons: Annotated[CommonQueryParams, Depends()]):
    response = {}
    if commons.q:
        response.update({'q': commons.q})
    items = fake_items_db[commons.skip: commons.skip + commons.limit]
    response.update({'items': items})
    return response
