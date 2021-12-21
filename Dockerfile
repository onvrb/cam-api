FROM python:3.9-alpine

COPY root/ /
WORKDIR /app

CMD [ "python3", "-u", "run.py"]
