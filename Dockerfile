FROM python:latest

WORKDIR /app
COPY app/* .

CMD ["prog-iter.py"]

ENTRYPOINT ["python3"]
