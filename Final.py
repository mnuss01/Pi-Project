import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep
def button_callback(channel):
    print("Button was pushed!")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW)
GPIO.add_event_detect(10, GPIO.RISING, callback = button_callback) 
while 10:
    GPIO.output(8, GPIO.HIGH)
    sleep(1)
    GPIO.output(8, GPIO.LOW)
    sleep(1)
message = input("Press enter to quit")
GPIO.cleanup()