from fastapi import FastAPI
from fastapi import File
from fastapi import UploadFile
from typing import Annotated
from typing import Union

app = FastAPI()
"""
@app.post('/files/')
async def create_file(file: Annotated[Union[bytes, None], File()] = None):
    if file:
        return {
            'file_size': len(file)
        }
    else:
        return {
            'message': 'No file sent'
        }
"""
"""
@app.post('/files/')
async def create_file(file: Annotated[bytes, File(description='A file read as bytes')]):
    return {
        'file_size': len(file)
    }
"""
@app.post('/files/')
async def create_file(files: Annotated[list[bytes], File(description='A file read as bytes')]):
    return {
        'file_sizes': [len(file) for file in files]
    }
"""
@app.post('/uploadfile/')
async def create_upload_file(file: Union[UploadFile, None] = None):
    if file:
        return {
            'filename': file.filename
        }
    else:
        return {
            'message': 'No upload file sent'
        }
"""
"""
@app.post('/uploadfile/')
async def create_upload_file(file: Annotated[UploadFile, File(description='A file read as UploadFile')]):
    return {
        'filename': file.filename
    }
"""
@app.post('/uploadfiles/')
async def create_upload_files(files: Annotated[list[UploadFile], File(description='A file read as UploadFile')]):
    return {
        'filenames': [file.filename for file in files]
    }
