from PIL import Image
import uuid
import os
from pathlib import Path
from io import BytesIO

def convert_to_webp(bytesIOImg):
    # In: file(BytesIO)
    # Out: PathToWebpImage
    image = Image.open(bytesIOImg)
    uid = uuid.uuid1()
    destinationFolder = './src/'+ str(uid)
    os.mkdir(destinationFolder)
    
    width = image.width
    height = image.height

    originalSize = [width,height, 'o']
    halfSize = [int(width/2), int(height/2), 'l']
    quarterSize = [int(width/4), int(height/4), 'm']
    eighthSize = [int(width/8), int(height/8), 's']
    sizes = [originalSize,halfSize,quarterSize,eighthSize]
    for size in sizes:
        im_resize = image.resize((size[0], size[1]))
        im_resize.save(destinationFolder+'/'+size[2]+'.webp')
    return str(uid)


def compress(imageBytes, options=["webp"]):
    byteImgIO = BytesIO(imageBytes)
    pathToCompressedImage = convert_to_webp(bytesIOImg=byteImgIO)
    return pathToCompressedImage