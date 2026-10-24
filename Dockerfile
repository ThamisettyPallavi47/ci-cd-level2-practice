
FROM python:3.12-slim

WORKDIR /app

COPY app.py .

CMD ["python", "-c", "from app import calculate_average; print(calculate_average([80, 90, 100]))"]
