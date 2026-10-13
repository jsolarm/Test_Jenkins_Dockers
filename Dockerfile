FROM python:3.12-slim

WORKDIR /app

COPY app.py .
COPY test_app.py .

CMD ["python", "app.py"]
