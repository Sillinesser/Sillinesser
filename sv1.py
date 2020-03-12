import RPi.GPIO as GPIO #імпортуємо бібліотеку для контролюванням GPIO виходів/входів на платі
import time             #імпортуємо клас ...., щоб застосовувати затримки

r1 = 2   #змінним для зручності присвоюєм номер пінів
y1 = 6
g1 = 10


GPIO.setmode(GPIO.BCM)   #ініціалізація входів/виходів

GPIO.setup(r1, GPIO.OUT)   #описуєм характер піну (вхід/вихід)
GPIO.setup(y1, GPIO.OUT)
GPIO.setup(g1, GPIO.OUT)



def sv1(sleep_red, sleep_green):     #функція циклу одного світлофору, на вхід якої подаємо два значення,
    GPIO.output(r1,1) #red 1         час затримки червоного та зеленого світла
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

    
    
    

    