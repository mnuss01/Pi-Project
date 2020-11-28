import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
def button_callback(channel):
    print("Button was pressed!")
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) # Pin number 10
GPIO.setup(8, GPIO.OUT, initial = GPIO.LOW) # Pin number 8
GPIO.add_event_detect(10, GPIO.RISING, callback = button_callback) 
while True:
    if GPIO.event_detected(10):
        print(" LED is on.")
        activate = True
        while (activate is True):
            GPIO.output(8, GPIO.HIGH)
            if GPIO.event_detected(10):
                activate = False
        else:
            GPIO.output(8, GPIO.LOW)
            print(" LED is off.")
GPIO.cleanup()