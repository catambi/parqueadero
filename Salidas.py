import RPi.GPIO as GPIO
import time

def luzVerde():
    lVerde=13
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(lVerde,GPIO.OUT)
    GPIO.output(lVerde,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(lVerde,GPIO.LOW)
        
def luzRoja():
    lRoja=11
    GPIO.cleanup()
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(lRoja,GPIO.OUT)
    GPIO.output(lRoja,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(lRoja,GPIO.LOW)
  

