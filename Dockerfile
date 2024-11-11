# Utilizar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el script al contenedor
COPY Counter.py /app/Counter.py

# Ejecutar el script
CMD ["python", "/app/Counter.py"]
