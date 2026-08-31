FROM python:3.12

WORKDIR /app

COPY . .

CMD ["python", "main.py"]