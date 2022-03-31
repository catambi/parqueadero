import RPi.GPIO as GPIO
import time
import barrera
import Salidas
import GeneradorCodigoBarras
def EntradaL():
    salRele=GPIO.input(16)
    RB01=GPIO.input()
    while True:
        if (salRele==True)and(RB01==0):
            Salidas.luzVerde()
            #GeneradorCodigoBarras.imprimir()
            barrera.Entrada()
            break
        elif (RB01==1):
            Salidas.luzRoja()
            break