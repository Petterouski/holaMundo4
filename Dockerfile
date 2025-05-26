# Usa una imagen oficial de Python
FROM python:3.10-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código fuente
COPY . .

# Puerto por donde se expone la app
EXPOSE 5000

# Comando para iniciar la aplicación
CMD ["gunicorn", "app:app"]
