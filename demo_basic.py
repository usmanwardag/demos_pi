import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# GPIO.setmode(GPIO.BCM)

GPIO.setup(16, GPIO.OUT)
LED_STATUS = False 

while True:
    try:
        GPIO.output(16, LED_STATUS)
        time.sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

