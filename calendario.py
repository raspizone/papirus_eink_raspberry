import calendar
import datetime
from papirus import PapirusComposite

def obtener_mes_anio_actual():
    ahora = datetime.datetime.now()
    mes = ahora.month
    anio = ahora.year
    return mes, anio

def obtener_calendario(mes, anio):
    cal = calendar.monthcalendar(anio, mes)
    return cal

def obtener_nombre_mes(mes):
    return calendar.month_name[mes]

def obtener_dia_actual():
    hoy = datetime.datetime.now()
    return hoy.day

screen = PapirusComposite(rotation=0)

mes, anio = obtener_mes_anio_actual()

calendario = obtener_calendario(mes, anio)

nombre_mes = obtener_nombre_mes(mes)

dia_actual = obtener_dia_actual()

screen.AddText(f"{nombre_mes} {anio}", 10, 10, Id="nombre_mes")

y_offset = 40

for semana in calendario:
    for i, dia in enumerate(semana):
        if dia != 0:  
            if dia == dia_actual:
                screen.AddText(f"[{dia}]", 10 + (i * 30), y_offset, Id=f"dia_{dia}_actual", size=24)
            else:
                screen.AddText(str(dia), 10 + (i * 30), y_offset, Id=f"dia_{dia}")
    y_offset += 30  

screen.WriteAll()
