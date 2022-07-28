'''
This module takes a picture using the raspberry pi camera module
'''

from picamera import PiCamera
import time

# start a camera module
camera = PiCamera()

# flip the camera 180 degrees
camera.rotation = 180

camera.start_preview()
# camera needs at least 2 seconds for capturing a still
time.sleep(5)

# name the picture according to the specific time string at which it was taken
name = str(int(time.time()))
camera.capture(name+'.jpg')
camera.stop_preview()

print('Picture taken. File named:'+name+'.jpg')
