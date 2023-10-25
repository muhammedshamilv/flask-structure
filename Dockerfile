FROM python:3.10.6-alpine3.16
RUN apk add git build-base linux-headers libffi-dev
WORKDIR /structure\ app

RUN sudo apt-get update && sudo apt-get install -f -y postgresql-client

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

CMD ["python","run.py"]