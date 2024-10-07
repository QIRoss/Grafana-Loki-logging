import logging
from os import getenv
from fastapi import FastAPI
from multiprocessing import Queue
from logging_loki import LokiQueueHandler

app = FastAPI()

loki_logs_handler = LokiQueueHandler(
    Queue(-1),
    url=getenv("LOKI_ENDPOINT"),
    tags={"application": "fastapi"},
    version="1",
)

uvicorn_access_logger = logging.getLogger("uvicorn.access")
uvicorn_access_logger.addHandler(loki_logs_handler)

@app.get("/")
async def root():
    return {"message": "Hello World"}