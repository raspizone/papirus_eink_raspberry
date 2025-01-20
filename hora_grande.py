import time
import datetime
from papirus import PapirusTextPos
from PIL import ImageFont

text = PapirusTextPos(rotation=0)

font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"  
font_size = 80  
font = ImageFont.truetype(font_path, font_size)

def mostrar_reloj():
    while True:
        ahora = datetime.datetime.now()
        hora = ahora.strftime("%H:%M:%S")  

        text.Clear()

        text.AddText(hora, fontPath=font_path, size=font_size)

        time.sleep(60)

mostrar_reloj()
