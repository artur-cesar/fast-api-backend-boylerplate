# Dockerfile
FROM {{ docker_image or "python:3.12-slim" }}

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./app ./app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "{{ api_port or 8000 }}", "--reload"]
