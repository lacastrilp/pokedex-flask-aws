from flask import Flask
from .routes import json_route, image_route

def create_app():
    app = Flask(__name__)

    # Registro de rutas
    app.add_url_rule("/pokenea", view_func=json_route)
    app.add_url_rule("/pokenea-image", view_func=image_route)

    return app