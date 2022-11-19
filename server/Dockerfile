FROM python:3.8-slim AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get upgrade -y

RUN apt-get install tesseract-ocr -y&& \
    apt-get install tesseract-ocr-eng -y &&\
    apt-get install tesseract-ocr-rus -y 
RUN apt-get install libgl1-mesa-glx -y
## install python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

## copy source code
COPY . .
# RUN ls -a
ENV PATH="/opt/venv/bin:$PATH"

## Start the uvicorn server and alembic migrations
CMD ["sh", "-c" , "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]