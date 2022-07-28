'''
This is the first script for remote controlling the raspi cart using through
a secured shell connection (ssh) [Created 2019/04/12]
'''

# import the motor controlling functions developed
from motor import *
import ultrasound_crash as us_crash
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


d = 300

#create empty data string
data = [0, 0, 0]
# creating the main loop
while True:

    # set an infinite loop to go forward until distance is less than 30 cm
    while d > 30:
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

        # get distance reading, append to data
        data.append(us_crash.get_distance())

        # calculate the distance as the average of the last 3 measurements to reduce sensor noise
        d = (1/3)*(data[-3]+data[-2]+data[-1])

        # end loop in case data is wrong
        if d <= 1:
            break
    # if distance is too close to the wall
    else:
        # stop all motion
        time.sleep(3)

        # go backwards
        reverse(2.5)

        # turn
        right_turn(2.5)

        # set d larger again to go out of this loop
        d = 31
