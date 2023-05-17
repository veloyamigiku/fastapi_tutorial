from fastapi import Depends
from fastapi import FastAPI
from fastapi import Header
from fastapi import HTTPException
from typing import Annotated

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

app = FastAPI(dependencies=[Depends(verify_token), Depends(verify_key)])

@app.get('/health_check')
async def check_health():
    return {
        'health_check': 'ok'
    }

@app.get('/items/')
async def read_items():
    return [
        {
            'item': 'Plumbus'
        },
        {
            'item': 'Portal Gun'
        }
    ]

@app.get('/users/')
async def read_users():
    return [
        {
            'username': 'Rick'
        },
        {
            'username': 'Morty'
        }
    ]
