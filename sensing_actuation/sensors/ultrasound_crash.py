'''
This file runs uses the raspberry pi to collect data using an hc-sr05 ultrasound sensor.
'''
import RPi.GPIO as gpio
import time
from motor import *

TRIG = 16
ECHO = 20

# Initialize the pins to output commands to the ultrasound sensor
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(TRIG,gpio.OUT)
    gpio.setup(ECHO,gpio.IN)
    print("HC-SR05 Sensor Activated")

def get_distance():
    init()
    # ensure trigger pin is set to low
    gpio.output(TRIG, False)
    # print("Waiting For Sensor To Settle")
    time.sleep(0.25)

    # sensor requires 10micro secs to trigger the module -> (8 sound bursts at 40kHz)
    # set trigger to high to send pulse
    gpio.output(TRIG, True)
    time.sleep(0.00001)
    gpio.output(TRIG, False)

    while gpio.input(ECHO)==0:
        pulse_start = time.time()

    while gpio.input(ECHO)==1:
        pulse_end = time.time()

    # This is the time for a pulse to travel and come back. Thus, divide by two
    pulse_duration = (pulse_end - pulse_start)/2

    # Get distance by multiplying by speed of sound. 343m/s = dist/time
    distance = pulse_duration * 34300 #cm/s at sea level
    distance = round(distance, 2)
    # print("Distance:",distance,"cm")
    return distance
    gpio.cleanup()


# testing the proper working of the Sensor
if __name__ == '__main__':
    '''
    test program is working properly
    '''
    x = [x for x in range(10)]
    for i in x:
        d = get_distance()
        print(d)
        time.sleep(0.2)

        # test ability to control motor while runing sensor
        if d > 50:
            forward(0.5)
        elif d < 10:
            reverse(0.5)
        else:
            pass
