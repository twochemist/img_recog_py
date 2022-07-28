'''
This script goes over the main functionality of the self-driving pi V 0.2.1
this version includes a camera module, and can take pictures on command.
'''

import RPi.GPIO as GPIO
import time
import button_press
import send_email
import take_pic_for_email
from datetime import datetime

name = datetime.now().strftime("%H_%M_on_%Y-%m-%d")
# run an infinite loop.
while True:
    if button_press.picture_button() == True:
        name = take_pic_for_email.take_pic()
        send_email.sendpic(name)
        print('picture sent')
        time.sleep(0.2)
    else:
        pass
