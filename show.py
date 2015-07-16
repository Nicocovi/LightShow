
#!/usr/bin/env python

# Import required Python libraries
import RPi.GPIO as GPIO
import time
from random import randint


# Use BCM GPIO references instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(9,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)


GPIO.output(4,0)
GPIO.output(9,0)
GPIO.output(10,0)
GPIO.output(11,0)
GPIO.output(22,0)

randomVar = randint(10,20)
count = 0
switches = randint(6,10)
arrayGpio = array([4,9,10,11,22])

while count < switches:
	count = count + 1
	time.sleep(1)
	print ("Counting")



       	




