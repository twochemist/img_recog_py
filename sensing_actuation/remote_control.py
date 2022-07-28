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
lag = 0.1

print('-'*20+
'\npi-cart has been activated for remote access'
'\nPlease move using the asdw arrow commands'
'\nTo quit, press q'+
'-'*20)
# creating the main loop
while True:


'''
    # moving forward
    if keyboard.is_pressed('w'):
        print('moving forward')
        forward(lag)
        time.sleep(lag)

    # moving backwards
    elif keyboard.is_pressed('s'):
        print('going backwards')
        reverse(lag)
        time.sleep(lag)

    # turning right
    elif keyboard.is_pressed('d'):
        print('turning right')
        right_turn(lag)
        time.sleep(lag)

    elif keyboard.is_pressed('a'):
        print('turning left')
        left_turn(lag)
        time.sleep(lag)

    elif keyboard.is_pressed('q'):
        print('Exiting remote control')
        break

    else:
        print('working but waiting')
        time.sleep(lag)
'''
