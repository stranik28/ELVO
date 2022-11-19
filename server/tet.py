import cv2
import numpy as np
import os

import pytesseract as tess


# async def check_passport(file: UploadFile):
#     contents = await file.read()
#     nparr = np.fromstring(contents, np.uint8)
#     img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#     img = cv2.threshold(img, 0, 255, cv2.THRESH_TOZERO)[1]
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     filename = "{}.png".format("temp")
#     cv2.imwrite(filename, img)
#     text = pytesseract.image_to_string(img, lang="rus+eng")
#     return text

img = cv2.imread('src/ptsp.png')
img = cv2.threshold(img, 0, 255, cv2.THRESH_TOZERO)[1]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
filename = "{}.png".format("temp")
cv2.imwrite(filename, img)
text = tess.image_to_string(img, lang="rus+eng")
print(text)