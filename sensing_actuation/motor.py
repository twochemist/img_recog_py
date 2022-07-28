'''
The following code has been optimized to work with the Self Driving Pi autonomous driving car developed by
Fidel Esquivel Estay. For more information, visit www.fidelesquivel.com or www.github.com/phideltaee/self-driving-pi.git
'''

# __author__ =
# __metadata__ =

import RPi.GPIO as gpio
import time

# Outs 23,24 correspond to OUT3, OUT4 in L298N driver
# likewise, 17, 22 correspond to OUT1, OUT2 in driver.
OUT1 = 17
OUT2 = 22
OUT3 = 23
OUT4 = 24

# Initialize the pins to output commands to the motor controller
def init():
    gpio.setmode(gpio.BCM)
    gpio.setup(OUT1,gpio.OUT)
    gpio.setup(OUT2,gpio.OUT)
    gpio.setup(OUT3,gpio.OUT)
    gpio.setup(OUT4,gpio.OUT)

# Tell the motors to move forward. True and False values need to be tweeked while running
def forward(tf):
    init()
    gpio.output(OUT1, True)
    gpio.output(OUT2, False)
    gpio.output(OUT3, True)
    gpio.output(OUT4, False)
    time.sleep(tf)
    gpio.cleanup()

def reverse(tf):
    init()
    gpio.output(OUT1, False)
    gpio.output(OUT2, True)
    gpio.output(OUT3, False)
    gpio.output(OUT4, True)
    time.sleep(tf)
    gpio.cleanup()

def right_turn(tf):
    init()
    gpio.output(OUT1, False)
    gpio.output(OUT2, True)
    gpio.output(OUT3, True)
    gpio.output(OUT4, False)
    time.sleep(tf)
    gpio.cleanup()

def left_turn(tf):
    init()
    gpio.output(OUT1, True)
    gpio.output(OUT2, False)
    gpio.output(OUT3, False)
    gpio.output(OUT4, True)
    time.sleep(tf)
    gpio.cleanup()

if __name__ == "__main__":
    ''' This script tests that the motor driver is working properly'''
    t = 0.5
    forward(t)
    reverse(t)
    right_turn(t)
    left_turn(t)
    print('forward \nreverse \nright \nleft')
