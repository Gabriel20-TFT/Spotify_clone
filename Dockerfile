FROM python:3.11-slim

# Setează variabile de mediu
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Instalează dependențe de sistem pentru MySQL
RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Setează directorul de lucru
WORKDIR /app

# Copiază requirements și instalează dependențele Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiază tot proiectul
COPY . .

# Creează directoarele necesare
RUN mkdir -p /app/staticfiles /app/media /app/logs

# Expune portul 8000
EXPOSE 8000

# Comandă default
CMD ["gunicorn", "spotify_clone.wsgi:application", "--bind", "0.0.0.0:8000"]
