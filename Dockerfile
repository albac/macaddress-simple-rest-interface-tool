FROM python:3.10-buster

ENV MACADDRESS=xxxxxx

ENV DEBUG=false

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]
