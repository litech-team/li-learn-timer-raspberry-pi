FROM python:3.10

RUN pip install websockets

ADD . /app
WORKDIR /app

CMD ["python", "-u", "main.py"]