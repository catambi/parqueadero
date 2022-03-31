import RPi.GPIO as GPIO
import time
import Salidas

def Entrada():
	GPIO.setmode(GPIO.BOARD)
	sPosicion1=0
	sPosicion2=0
	ActivarBarrera=36
	PINs1=18
	PINs2=22
	#GPIO.setup(PINB,GPIO.OUT)
	GPIO.setup(PINs2,GPIO.IN)
	GPIO.setup(ActivarBarrera,GPIO.OUT)
	GPIO.setup(PINs1,GPIO.IN)
	while True:
		sPosicion1=GPIO.input(18)
		sPosicion2=GPIO.input(22)
		if sPosicion1==1:
			GPIO.output(ActivarBarrera,GPIO.HIGH)
			#print(ActivarBarrera)
		elif sPosicion2==1:
			GPIO.output(ActivarBarrera,GPIO.HIGH)
		else:
			time.sleep(3)
			GPIO.output(ActivarBarrera,GPIO.LOW)
			#print(SensorPosicion01)
			break
