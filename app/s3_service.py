# Logica de S3/Boto3

import os
import boto3

# Inicializa el cliente S3 (usa variables de entorno)
# El anexo del PDF da una idea de cómo se inicializa boto3
try:
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
        region_name=os.getenv("AWS_REGION"),
    )
    S3_BUCKET = os.getenv("S3_BUCKET")
    AWS_REGION = os.getenv("AWS_REGION")
except Exception as e:
    # Manejo de error si las variables de entorno no están cargadas (ej. local)
    s3_client = None
    S3_BUCKET = "pokenea-dummy-bucket"
    AWS_REGION = "us-east-1"
    print(f"Advertencia: Boto3 no inicializado completamente: {e}")

def get_pokenea_image_url(image_key):
    """Genera la URL pública para una imagen en S3."""
    # Como los elementos del bucket tienen acceso público,
    # se usa la URL de acceso directo (path-style o virtual-hosted style)
    if S3_BUCKET:
        # Formato de URL de S3: https://<bucket-name>.s3.<region>.amazonaws.com/<key>
        return f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{image_key}"
    return "url_de_imagen_falsa.jpg" # Fallback