'''
This module takes a picture using the raspberry pi camera module
'''

from picamera import PiCamera
import time
from datetime import datetime


# start a camera module
camera = PiCamera()

# flip the camera 180 degrees
camera.rotation = 180

def take_pic():
    camera.start_preview()
    # camera needs at least 2 seconds for capturing a still
    time.sleep(3)

    # name the picture according to the specific time string at which it was taken
    name = datetime.now().strftime("%H_%M_on_%Y-%m-%d")
    camera.capture(name+'.jpg')
    camera.stop_preview()
    return name
    print('Picture taken. File named:'+name+'.jpg')

if __name__ == "__main__":
    # to test this function, send the picture just taken to the email
    from send_email import sendpic
    name = take_pic()
    sendpic(name)
