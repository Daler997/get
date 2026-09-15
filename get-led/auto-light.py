import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

led = 26
foto = 6
GPIO.setup(foto, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

while True:
    GPIO.output(led, not GPIO.input(foto))