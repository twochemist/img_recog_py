'''
Pulse Width Modulation control for self-driving pi. Developed by
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

def speed(v):
    init()
    motor1_in1_pin = OUT1
    motor1_in2_pin = OUT2
    gpio.setup(motor1_in1_pin, gpio.OUT)
    gpio.setup(motor1_in2_pin, gpio.OUT)
    motor1 = gpio.PWM(OUT1,20)
    motor1.start(0)
    motor1.ChangeDutyCycle(v)

    motor2_in1_pin = OUT3
    motor2_in2_pin = OUT4
    gpio.setup(motor2_in1_pin, gpio.OUT)
    gpio.setup(motor2_in2_pin, gpio.OUT)
    motor2 = gpio.PWM(OUT3,20)
    motor2.start(0)
    motor2.ChangeDutyCycle(v)

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
    speed(10)
    time.sleep(tf)
    gpio.cleanup()

def right_turn(tf):
    init()
    gpio.output(OUT1, False)
    gpio.output(OUT2, True)
    gpio.output(OUT3, True)
    gpio.output(OUT4, False)
    speed(10)
    time.sleep(tf)
    gpio.cleanup()

def left_turn(tf):
    init()
    gpio.output(OUT1, True)
    gpio.output(OUT2, False)
    gpio.output(OUT3, False)
    gpio.output(OUT4, True)
    speed(20)
    time.sleep(tf)
    gpio.cleanup()

if __name__ == "__main__":
    ''' This script tests that the motor driver is working properly'''
    t = 0.5
    forward(t)
    reverse(t)
    right_turn(t+1)
    left_turn(t)
    print('forward \nreverse \nright \nleft')
    print('-'*20+'\nNow, pulse width modulation')

    print('now run for 2 seconds')
    time.sleep(2)
    print('done')
    gpio.cleanup()
    exit()
