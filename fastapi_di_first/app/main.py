from fastapi import Depends
from fastapi import FastAPI
from typing import Annotated
from typing import Union

app = FastAPI()

@app.get('/health_check')
async def check_health():
    return {
        'health_check': 'ok'
    }

async def common_parameters(
    q: Union[str, None] = None,
    skip: int = 0,
    limit: int = 100):
    return {
        'q': q,
        'skip': skip,
        'limit': limit
    }

CommonsDep = Annotated[dict, Depends(common_parameters)]

@app.get('/items/')
async def read_item(commons: CommonsDep):
    return commons

@app.get('/users/')
async def read_users(commons: CommonsDep):
    return commons
