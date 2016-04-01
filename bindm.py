import RPi.GPIO as GPIO
import time
import pykeyboard
from pykeyboard import PyKeyboard
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

k = PyKeyboard()

while True:
	input_state = GPIO.input(18)
	if input_state == False :
		print('Button Pressed')
		k.tap_key("m")
		#os.system ('aplay /home/pi/Desktop/ominogiallo/sirena.wav')
		time.sleep(0.2)
		k.tap_key('Tab')
		time.sleep(0.1)
		k.tap_key('Return')
		time.sleep(10)
