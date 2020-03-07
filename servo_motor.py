#Bibliotecas
import RPi.GPIO as GPIO
import time

#Configura denominação dos terminais
GPIO.setmode(GPIO.BCM)
servoPIN = 17
GPIO.setup(servoPIN, GPIO.OUT)
p = GPIO.PWM(servoPIN, 50)
p.start(0)

try:
    while True:
        for x in range (10):
            p.ChangeDutyCycle(x)
            time.sleep(0.1)
        
        for x in range (10):
            p.ChangeDutyCycle(10-x)
            time.sleep(0.1)
        
except KeyboardInterrupt:
    p.stop()
    GPIO.cleanup()