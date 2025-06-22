FROM python:3.10-slim-bullseye

WORKDIR /app

COPY . .

RUN apt-get update && apt-get upgrade -y && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888

CMD ["uvicorn","app.main:app","--host","0.0.0.0","--port","8888"]