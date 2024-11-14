# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo en /app
WORKDIR /app

# Copiar los archivos requeridos al contenedor
COPY kafka_consumer.py .
COPY requirements.txt .

# Instalar las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Establecer las variables de entorno (cargar archivo .env)
COPY .env /app/.env

# Ejecutar el consumidor de Kafka
CMD ["python", "kafka_consumer.py"]
