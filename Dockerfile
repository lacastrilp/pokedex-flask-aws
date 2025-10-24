# Usa una imagen base ligera de Python
FROM python:3.9-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /usr/src/app

# Copia los archivos de dependencia e instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Expone el puerto que usa la aplicación Flask (puerto 80)
EXPOSE 80

# Comando para ejecutar la aplicación
# Las variables de entorno de AWS serán inyectadas por Docker Swarm
CMD ["python", "run.py"]

