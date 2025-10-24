# Script para iniciar la app

import os
from dotenv import load_dotenv
from app import create_app

# Carga variables de entorno (solo para desarrollo local)
load_dotenv() 

app = create_app()

if __name__ == "__main__":
    # La aplicación se ejecuta en el host 0.0.0.0 y puerto 80
    # Esto es crucial para el despliegue en contenedores
    app.run(host="0.0.0.0", port=80)