import requests
import datetime
from papirus import PapirusComposite

def obtener_hora():
    ahora = datetime.datetime.now()
    hora = ahora.strftime("%H:%M:%S")  
    return hora

def obtener_fecha():
    ahora = datetime.datetime.now()
    fecha = ahora.strftime("%A, %d %B %Y")
    return fecha

def obtener_tiempo():
    api_key = '5fa050aaf8edc169a6c437a81dbf0a2f'
    location = 'Madrid'
    url = f'http://api.weatherstack.com/current?access_key={api_key}&query={location}'

    response = requests.get(url)
    data = response.json()

    temperature = data['current']['temperature']
    weather_descriptions = data['current']['weather_descriptions'][0]
    return f"El clima en {location} es: {weather_descriptions} con una temperatura de {temperature}°C"

screen = PapirusComposite(rotation=0)

hora = obtener_hora()
fecha = obtener_fecha()
tiempo = obtener_tiempo()

screen.AddText(f"Hora: {hora}", 10, 10, Id="hora")

screen.AddText(f"Fecha: {fecha}", 10, 40, Id="fecha")

screen.AddText(f"{tiempo}", 10, 90, Id="tiempo")

screen.WriteAll()

