import time
import picamera
#from datetime import datetime
from PIL import Image
import RPi.GPIO 
import io
import os
Light = 17
RPi.GPIO.setmode(RPi.GPIO.BCM)
RPi.GPIO.setup(Light,RPi.GPIO.IN)

camera = picamera.PiCamera()

def newimage() :       
        camera.capture('/home/pi/inst.jpg')
        print "captured " 
while 1:

	if  RPi.GPIO.input(Light)!=1:    #if the level is high, take  pictures
		if n==1:
			os.remove('/home/pi/inst.jpg') 
		newimage()
		n=1
		time.sleep(10)
		os.system('export PRINTER=pi1010')
		os.system('lp -d pi1010 inst.jpg')
		time.sleep(10)
	

