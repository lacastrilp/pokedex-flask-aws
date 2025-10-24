# Rutas de la aplicacion

import os
import socket
from flask import jsonify, render_template_string
from .pokenea_data import get_random_pokenea
from .s3_service import get_pokenea_image_url

# Obtiene el ID del contenedor/host
# En un contenedor Docker, os.uname()[1] o socket.gethostname() suele dar el ID del contenedor.
def get_container_id():
    return socket.gethostname()

# Definición de la primera ruta: JSON con datos
def json_route():
    pokenea = get_random_pokenea()
    # Se pide incluir solo id, nombre, altura, y habilidad
    data_json = {
        "id": pokenea["id"],
        "nombre": pokenea["nombre"],
        "altura": pokenea["altura"],
        "habilidad": pokenea["habilidad"],
        "contenedor_id": get_container_id() # Incluir id del contenedor
    }
    return jsonify(data_json)

# Definición de la segunda ruta: Imagen y frase filosófica
def image_route():
    pokenea = get_random_pokenea()
    image_url = get_pokenea_image_url(pokenea["imagen"])
    container_id = get_container_id()

    # Muestra por pantalla la imagen y la frase filosófica
    # y el id del contenedor
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Pokenea Aleatorio</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
            .pokenea-card { border: 1px solid #ccc; padding: 20px; border-radius: 10px; display: inline-block; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
            img { max-width: 300px; height: auto; border-radius: 5px; }
            .phrase { font-style: italic; margin-top: 15px; font-size: 1.2em; }
            .container-info { margin-top: 25px; font-size: 0.8em; color: #666; }
        </style>
    </head>
    <body>
        <div class="pokenea-card">
            <h1>{{ pokenea_nombre }}</h1>
            <img src="{{ image_url }}" alt="Imagen de {{ pokenea_nombre }}">
            <p class="phrase">"{{ pokenea_frase }}"</p>
        </div>
        <p class="container-info">Servido desde Contenedor ID: <strong>{{ container_id }}</strong></p>
    </body>
    </html>
    """

    return render_template_string(
        html_template,
        pokenea_nombre=pokenea["nombre"],
        image_url=image_url,
        pokenea_frase=pokenea["frase_filosofica"],
        container_id=container_id
    )