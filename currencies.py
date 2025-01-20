import requests
from bs4 import BeautifulSoup
from papirus import PapirusComposite
from PIL import Image

def obtener_tipo_cambio():
    api_key = 'bc6f5497a1c1ec7116e0f1eddb594173'
    url = f'https://api.exchangerate.host/convert?access_key={api_key}&from=USD&to=EUR&amount=1'


    response = requests.get(url)
    data = response.json()

    euro_dollar_rate = data['result']
    return f"EUR/USD: {euro_dollar_rate}"

def obtener_precio_cripto(cripto="bitcoin"):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={cripto}&vs_currencies=usd"
    response = requests.get(url)
    data = response.json()
    
    if cripto in data:
        precio = data[cripto]["usd"]
        return f"Precio de {cripto.capitalize()}: ${precio}"
    else:
        return "No se pudo obtener el precio."

def convertir_a_bmp(image_path):
    img = Image.open(image_path)
    bmp_path = image_path.split('.')[0] + ".bmp"
    img.save(bmp_path, "BMP")
    return bmp_path

screen = PapirusComposite(rotation=0)

informacion_cripto = obtener_precio_cripto("bitcoin")
informacion_cambio = obtener_tipo_cambio()

screen.AddText(informacion_cripto, 10, 10, Id="info_cripto")
screen.AddText(informacion_cambio, 10, 50, Id="info_sp500")

image_path = "/home/pi/Downloads/btc.png"  # Cambia esta ruta por la de tu imagen
bmp_image_path = convertir_a_bmp(image_path)

screen.AddImg(bmp_image_path, 150, 80, (100, 100), Id="imagen_financiera")

screen.WriteAll()
