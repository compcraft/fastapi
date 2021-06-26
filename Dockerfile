FROM python:3.8-alpine
WORKDIR /src

#COPY src .
COPY requirements.txt requirements.txt

RUN apk add --no-cache --virtual .build-deps gcc libc-dev make bash \
    && pip install --no-cache-dir "uvicorn[standard]" gunicorn \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del .build-deps gcc libc-dev make bash

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]
