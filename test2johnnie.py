"""
Programa para propuesta uno Johnnie Walker
Control de aumento de barra led de acuerdo al porcentaje de avance
Control de led 7 segmentos de acuerdo a la hora  
"""
import time
import board
import neopixel
from datetime import datetime
# Inicializacion de ariables
horario_inicio = [9,15]
horario_cerrado = [18,45]
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
# Para el neopixel de barra
pin_barra_aumento = board.D21
# Para la hora
pin_decena_hora = board.D12
# Para el minuto
pin_decena_minuto = board.D18
# Estos valores deben cambiar segun lo estimado en el diseno
num_pixels_ba = 10
num_pixels_dh = 14
num_pixels_dm = 14
# Esto no se que hace
ORDER = neopixel.GRB
# Iniciacion de pixels
barra_aumento = neopixel.NeoPixel(pin_barra_aumento, num_pixels_ba, brightness=1, auto_write=True, pixel_order=ORDER)
decena_hora = neopixel.NeoPixel(pin_decena_hora, num_pixels_dh, brightness=1, auto_write=True, pixel_order=ORDER)
decena_minu = neopixel.NeoPixel(pin_decena_minuto, num_pixels_dm, brightness=1, auto_write=True, pixel_order=ORDER)
#programa principal
def principal():
    #vemos la hora de pc y separamos por digito
    digito_horad = int(horario_cerrado[0] / 10) - int(datetime.now().hour / 10) 
    digito_horau = (horario_cerrado[0] % 10) - (datetime.now().hour % 10)
    digito_minud = int(horario_cerrado[1] / 10) - int(datetime.now().minute / 10)
    digito_minuu = (horario_cerrado[1] % 10) - (datetime.now().minute % 10)
    # Impresion de datos, solo para verificar
    print(digito_horad, digito_horau, digito_minud, digito_minuu)
    
    # Llamamos a la funcion de imprimir e imprimimos el digito en el puerto
    siete_segmentos(digito_horad, decena_hora, 0)
    siete_segmentos(digito_horau, decena_hora, 7)
    decena_hora.show()
    siete_segmentos(digito_minud, decena_minu, 0)
    siete_segmentos(digito_minuu, decena_minu, 7)
    decena_minu.show()
    # establecemos nivel de barra led de acuerdo con el horario
    hora_i = horario_inicio[0] + horario_inicio[1]/60
    hora_f = horario_cerrado[0] + horario_cerrado[1]/60
    rango_trabajo = hora_f - hora_i
    # Impresion solo para verificar
    print(rango_trabajo)
    
    #porcentaje de uso
    hora_actual = datetime.now().hour + datetime.now().minute / 60
    porcentaje = (hora_actual - hora_i) * 100 / rango_trabajo
    # Impresion para verificar
    print(porcentaje)
    
    # Llamamos a la funcion de imprimir e imprimimos el digito en el puerto
    porcentaje_aumento = num_pixels_ba * porcentaje / 100 
    barra_aumento = neopixel.NeoPixel(pin_barra_aumento, porcentaje_aumento, brightness=1, auto_write=True, pixel_order=ORDER)
    barra_aumento.fill((0,255,0))
    
# Para esta funcion cada chip es un segmento
# Solicita el numero y el pin de salida
# Solicitamos el num que indica si es 0 = decena 1 = unidad
def siete_segmentos(val,pixel,num):
    # Casos de numeros
    if (val == 0):
        # 0
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (255,0,0)
        pixel[4+num] = (255,0,0)
        pixel[5+num] = (255,0,0)
        pixel[6+num] = (0,0,0)
        print("0")
    elif (val == 1):
        # 1
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (0,0,0)
        pixel[3+num] = (0,0,0)
        pixel[4+num] = (0,0,0)
        pixel[5+num] = (0,0,0)
        pixel[6+num] = (0,0,0)
        print("1")
    elif (val == 2):
        # 2
        pixel[0+num] = (0,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (0,0,0)
        pixel[4+num] = (255,0,0)
        pixel[5+num] = (255,0,0)
        pixel[6+num] = (255,0,0)
        print("2")
    elif (val == 3):
        # 3
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (0,0,0)
        pixel[4+num] = (0,0,0)
        pixel[5+num] = (255,0,0)
        pixel[6+num] = (255,0,0)
        print("3")
    elif (val == 4):
        # 4
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (0,0,0)
        pixel[3+num] = (255,0,0)
        pixel[4+num] = (0,0,0)
        pixel[5+num] = (0,0,0)
        pixel[6+num] = (255,0,0)
        print("4")
    elif (val == 5):
        # 5
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (0,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (255,0,0)
        pixel[4+num] = (0,0,0)
        pixel[5+num] = (255,0,0)
        pixel[6+num] = (255,0,0)
        print("5")
    elif (val == 6):
        # 6
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (0,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (255,0,0)
        pixel[4+num] = (255,0,0)
        pixel[5+num] = (255,0,0)
        pixel[6+num] = (255,0,0)
        print("6")
    elif (val == 7):
        # 7
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (0,0,0)
        pixel[4+num] = (0,0,0)
        pixel[5+num] = (0,0,0)
        pixel[6+num] = (0,0,0)
        print("7")
    elif (val == 8):
        # 8
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (255,0,0)
        pixel[4+num] = (255,0,0)
        pixel[5+num] = (255,0,0)
        pixel[6+num] = (255,0,0)
        print("8")
    elif (val == 9):
        # 9
        pixel[0+num] = (255,0,0)
        pixel[1+num] = (255,0,0)
        pixel[2+num] = (255,0,0)
        pixel[3+num] = (255,0,0)
        pixel[4+num] = (0,0,0)
        pixel[5+num] = (0,0,0)
        pixel[6+num] = (255,0,0)
        print("9")
    else:
        # apaga todo
        pixel[0+num] = (0,0,0)
        pixel[1+num] = (0,0,0)
        pixel[2+num] = (0,0,0)
        pixel[3+num] = (0,0,0)
        pixel[4+num] = (0,0,0)
        pixel[5+num] = (0,0,0)
        pixel[6+num] = (0,0,0)
        print("e")

while True:
    principal()