FROM tiangolo/uvicorn-gunicorn-fastapi:latest

COPY main.py /app

COPY requirements.txt /app

RUN pip install -r /app/requirements.txt