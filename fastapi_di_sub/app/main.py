from fastapi import Cookie
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

def query_extractor(q: Union[str, None] = None):
    return q

def query_or_cookie_extractor(
    q: Annotated[str, Depends(query_extractor)],
    last_query: Annotated[Union[str, None], Cookie()] = None):
    if not q:
        return last_query
    else:
        return q

@app.get('/items/')
async def read_query(query_or_default: Annotated[str, Depends(query_or_cookie_extractor)]):
    return {
        'q_or_cookie': query_or_default
    }
