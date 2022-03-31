import RPi.GPIO as GPIO
import time
from time import sleep
import serial
import barrera
import Salidas
import biometrico

GPIO.setmode(GPIO.BOARD)
#GPIO.setwarnings(False)
salRele=0
PIN=16
GPIO.setup(PIN,GPIO.IN)
RB02=0
RB01=0

# def validGPIO(puerto,ingreso):
# 	if(ingreso):
# 		GPIO.setup(punto,GPIO.IN)
# 	else:
# 		GPIO.setup(punto,GPIO.OUT)
# 	return GPIO.input(punto)

while True:
    try:
        GPIO.setup(16,GPIO.IN)
        salRele=GPIO.input(16)
        if (salRele==True):
            #GPIO.output(RB01,GPIO.HIGH)
            biometrico.EntradaB()
        else:
            RB01=0
            #GPIO.output(RB01,GPIO.LOW)
        
    except KeyboardInterrupt:
        continue
        GPIO.cleanup()