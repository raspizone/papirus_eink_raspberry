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

screen = PapirusComposite(rotation=0)

hora = obtener_hora()
fecha = obtener_fecha()

screen.AddText(f"Hora: {hora}", 10, 10, Id="hora")

screen.AddText(f"Fecha: {fecha}", 10, 40, Id="fecha")

screen.WriteAll()

import time
while True:
    hora_actualizada = obtener_hora()
    screen.UpdateText("hora", f"Hora: {hora_actualizada}")
    screen.WriteAll()
    time.sleep(30)  
