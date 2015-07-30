
#!/usr/bin/env python

# Import required Python libraries
import RPi.GPIO as GPIO
import time
import random


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

random.seed()
count = 0
arrayGpio = [4,9,10,11,22]
switches = random.randint(20,30)
randomLight = random.randint(0,4)

while count < switches:
	count = count + 1
	GPIO.output(arrayGpio[randomLight], 1)
	time.sleep(1)
	GPIO.output(arrayGpio[randomLight], 0)
	switches = random.randint(20,30)
	randomLight = random.randint(0,4)
	print ("Counting", count)
print("Finish")

       	




