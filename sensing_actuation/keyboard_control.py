'''
This is the first script for remote controlling the raspi cart using through
a secured shell connection (ssh) [Created 2019/04/12]
'''

# import the motor controlling functions developed
from motor import *

# import the python keyboard library for key-directional input
import keyboard
import time, termios, sys, tty

# using the getch method to get keyboard input
# source: https://www.instructables.com/id/Controlling-a-Raspberry-Pi-RC-Car-With-a-Keyboard/
# The getch method can determine which key has been pressed
# by the user on the keyboard by accessing the system files
# It will then return the pressed key as a variable
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


#define lag
lag = float(input('define lag, between 0 to 1: '))
speed = float(input('speed, between 0.01 and 1: '))
assert speed >= 0 and speed <= 1

print('-'*20+
'\npi-cart has been activated for remote access'
'\nPlease move using the asdw arrow commands'
'\nTo quit, press q'+
'-'*20)



# creating the main loop
while True:
    char = getch()
    # moving forward
    if char == 'w':
        print('moving forward')
        forward(speed)
        time.sleep(lag)

    # moving backwards
    elif char == 's':
        print('going backwards')
        reverse(speed)
        time.sleep(lag)

    # turning right
    elif char == 'd':
        print('turning right')
        right_turn(speed)
        time.sleep(lag)

    elif char == 'a':
        print('turning left')
        left_turn(speed)
        time.sleep(lag)

    elif char == 'q':
        print('Exiting remote control')
        break

    else:
        print('working but waiting')
        time.sleep(lag)
