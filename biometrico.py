import RPi.GPIO as GPIO
import time
import barrera
import Salidas
#import GeneradorCodigoBarras
def EntradaB():
    PINR2=10
    GPIO.setup(PINR2,GPIO.IN)
    GPIO.setup(16,GPIO.IN)
    salRele=GPIO.input(16)
    RB02=GPIO.input(10)
    while True:
        if (salRele==True)and(RB02==0):
            Salidas.luzVerde()
            #GeneradorCodigoBarras.imprimir()
            barrera.Entrada()
            break
        elif (RB02==1):
            Salidas.luzRoja()
            break