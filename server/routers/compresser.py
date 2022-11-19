from importlib.resources import path
from fastapi import APIRouter, File, UploadFile, Depends, HTTPException

from services.compresser import compress

router = APIRouter(prefix="/compress", tags=["Compress"])

@router.post("/")
async def compress_image(image: UploadFile = File()):
    imageByte = compress(image.file.read())
    return imageByte