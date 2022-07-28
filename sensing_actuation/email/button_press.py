'''
This script detects when a button has been pressed on the raspberry pi, and takes
and emails a picture if so
'''

import RPi.GPIO as GPIO
import time

def init():
    GPIO.setmode(GPIO.BCM)

    # GPIO number for switch pin
    switch_pin = 21

    GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
'''
while True:
    input_state = GPIO.input(switch_pin)
    if input_state == False:
        print('button pressed')
        time.sleep(0.2)
'''
def picture_button():
    init()
    # read pin state
    input_state = GPIO.input(switch_pin)
    # if the connection has been made,
    if input_state == False:
        return True
