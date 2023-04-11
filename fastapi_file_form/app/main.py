from fastapi import FastAPI
from fastapi import File
from fastapi import Form
from fastapi import UploadFile
from typing import Annotated
from typing import Union

app = FastAPI()

@app.get('/health_check')
async def check_health():
    return {
        'health_check': 'ok'
    }

@app.post('/files/')
async def create_file(
    file: Annotated[bytes, File()],
    fileb: Annotated[UploadFile, File()],
    token: Annotated[str, Form()]):

    return {
        'file_size': len(file),
        'token': token,
        'fileb_content_type': fileb.content_type
    }
