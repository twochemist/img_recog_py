'''
This script does a full revolution for a stepper motor 28BYJ-48 using a ULN2003
motor driver.

Note: code adapted from https://www.youtube.com/watch?v=Dc16mKFA7Fo
'''
import RPi.GPIO as GPIO
import time

GPIO.setmode (GPIO.BCM)

ControlPin = [5,6,13,19]

for pin in ControlPin:
    GPIO.setup (pin, GPIO.OUT)
    GPIO.output (pin, 0)

seg = [ [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

# This is due to the gear ratio of 1-64 reduction. A full rotation
# will be 64*8 = 512 steps (using the half-step method)
for i in range (512):

    # Iterate through the 8 half-steps (elements of "seg")
    for halfstep in range (8):

        # Each half step (i.e [1,0,0,1] has 4 elements, iterate through these)
        for pin in range (4):

            # Set the pin outputs to the desired cycle
            GPIO.output (ControlPin[pin], seg[halfstep][pin])
            time.sleep (0.001)

GPIO.cleanup()
