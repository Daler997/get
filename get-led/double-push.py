import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = list(reversed([24, 22, 23, 27, 17, 25, 12, 16]))
GPIO.setup(leds, GPIO.OUT)

buttonUP = 9
buttonDOWN = 10
GPIO.setup([buttonUP, buttonDOWN],  GPIO.IN)

GPIO.output(leds, 0)

num = 0
sleep_time = 0.2
while True:
    if GPIO.input(buttonUP) and GPIO.input(buttonDOWN):
        num = 255
    elif GPIO.input(buttonDOWN):
        num -=1
        if num <= -1:
            num = 255
    elif GPIO.input(buttonUP):
        num += 1
        if num >= 256:
            num = 0
    GPIO.output(leds, [int(i) for i in bin(num)[2:].zfill(8)])
    time.sleep(sleep_time)