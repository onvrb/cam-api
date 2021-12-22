FROM python:3.9-alpine

RUN apk add --update --no-cache curl

COPY root/ /
WORKDIR /app

CMD [ "python3", "-u", "run.py"]
