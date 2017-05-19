#Librerias
from rrb3 import *
import RPi.GPIO as GPIO
import time
#Voltaje de la placa
rr = RRB3(5, 4)
#Ajuste de los puertos GPIO
GPIO.setmode(GPIO.BCM)

try:
	while True:
		d = rr.get_distancd()
		i = rr.get_distanci()
		rr.set_motors(0.7,0,0.7,0)
		if i < 21:
			rr.set_motors(0.5,0,0,0)
			time.sleep(0.1)
		if d < 21:
			rr.set_motors(0,0,0.5,0)
			time.sleep(0.1)
			

except KeyboardInterrupt:
	print("Saliendo de obstaculos")
	GPIO.cleanup()
