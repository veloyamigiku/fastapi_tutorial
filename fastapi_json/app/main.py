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

fake_db = {}

class Item(BaseModel):
    name: str
    timestamp: datetime
    description: Union[str, None] = None

@app.put('/items/{id}')
def update_item(id: str, item: Item):
    print(item)
    json_compatible_item_data = jsonable_encoder(item)
    print(json_compatible_item_data)
    fake_db[id] = json_compatible_item_data
