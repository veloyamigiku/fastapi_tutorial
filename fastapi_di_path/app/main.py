from fastapi import Depends
from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from typing import Annotated

app = FastAPI()

@app.get('/health_check')
async def check_health():
    return {
        'health_check': 'ok'
    }

async def verify_token(x_token: Annotated[str, Header()]):
    if x_token != 'fake-super-secret-token':
        raise HTTPException(
            status_code=400,
            detail='X-Token header invalid')
    print('verify_token_ok')

async def verify_key(x_key: Annotated[str, Header()]):
    if x_key != 'fake-super-secret-key':
        raise HTTPException(
            status_code=400,
            detail='X-Key header invalid')
    print('verify_key_ok')
    return x_key

@app.get('/items/', dependencies=[
    Depends(verify_token),
    Depends(verify_key)])
async def read_items():
    return [
        {
            'item': 'Foo'
        },
        {
            'item': 'Bar'
        }
    ]
