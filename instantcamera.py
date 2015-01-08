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
#timenow = datetime.now()
#filename = '/home/pi/instantp/' + "inst.jpg"#"m%02d%02d%02d.jpg" % (timenow.hour,timenow.minute,timenow.second)
def newimage() :       
        camera.capture('/home/pi/inst.jpg')
        print "captured " 
while 1:

	if  RPi.GPIO.input(Light)!=1:    #if the level is high, take N pictures
	
		os.remove('/home/pi/inst.jpg') 
		newimage()
		time.sleep(10)
		os.system('export PRINTER=pi1010')
		os.system('lp -d pi1010 inst.jpg')
		time.sleep(40)
	

