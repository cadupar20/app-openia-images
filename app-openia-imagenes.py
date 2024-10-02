import openai
import typer
import requests
from PIL import Image
from io import BytesIO

# Configura tu clave API
openai.api_key = 'tu_clave_api_aqui'

def analyze_image(image_path):
    # Cargar la imagen
    with open(image_path, "rb") as img_file:
        img_data = img_file.read()

    # Enviar la imagen a OpenAI para análisis (esto es un ejemplo conceptual)
    response = openai.Image.create(
        file=img_data,
        model="gpt-4-turbo",
        prompt="Detecta si cada uno de los humanos que estan en la imagen estan utilizando elementos de seguridad como ser cascos, zapatos de seguridad, mamelucos en esta imagen.",
        n=1,
        size="1024x1024"
    )
    
    return response 


def main():
    # Ruta a tu imagen
    image_path = 'images/imagen.jpg'
    result = analyze_image(image_path)
    
    # Imprimir el resultado del análisis
    print("Resultado del análisis:", result)


if __name__ == "__main__":
    print("Iniciando la app...")
    typer.run(main)