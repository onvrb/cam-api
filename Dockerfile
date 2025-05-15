FROM python:3.13-alpine

WORKDIR /app

COPY requirements.txt /app/requirements.txt

COPY src /app/src

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "python3", "-u", "src/run.py"]
