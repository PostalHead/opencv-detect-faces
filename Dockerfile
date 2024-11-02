FROM python:3.12.7-slim

WORKDIR /app

RUN apt-get update && apt-get install libgl1 libglib2.0-0 -y

RUN pip install opencv-python

COPY . .

ENTRYPOINT ["python","./main.py"]
