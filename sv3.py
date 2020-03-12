import RPi.GPIO as GPIO
import time

r1 = 4
y1 = 8
g1 = 12


GPIO.setmode(GPIO.BCM)

GPIO.setup(r1, GPIO.OUT)
GPIO.setup(y1, GPIO.OUT)
GPIO.setup(g1, GPIO.OUT)



def sv1(sleep_red, sleep_green):
    GPIO.output(r1,1) #red 1
    time.sleep(sleep_red)
    GPIO.output(y1,1) #yellow 1
    time.sleep(0.5)
    GPIO.output(r1,0) #red 1
    GPIO.output(y1,0) #yellow 1
    GPIO.output(g1,1) #green 1
    time.sleep(sleep_green)
    GPIO.output(g1,0) #green 1
    time.sleep(0.5)
    GPIO.output(g1,1) #green 1
    time.sleep(0.5)
    GPIO.output(g1,0) #green 1
    time.sleep(0.5)
    GPIO.output(g1,1) #green 1
    time.sleep(0.5)
    GPIO.output(g1,0) #green 1
    GPIO.output(r1,1) #red 1
    
    
 