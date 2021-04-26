FROM python:3.9.4-alpine

COPY . .

RUN chmod +x /example.py

ENV TZ Europe/Kiev

CMD python example.py