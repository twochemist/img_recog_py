'''
This script is the main control loop for the version 0.2.1 of the "Self-Driving Pi"
It calls to other libraries and modules developed by Fidel Esquivel Estay (PhiDeltaEE)

Hardware: 1 Raspberry Pi 3B +
          1 HC-SR05 Ultrasound sensor
          1 Raspberry camera module
          1 L298N Motor driver
          4 5V DC motors
          12V DC Power Supply

'''
# import raspberry pi gpio library, time and datetime libraries
import RPi.GPIO as GPIO
import time
from datetime import datetime

# import custom made libraries for taking pictures and sending emails
import camera_switch
import send_email
import take_pic_for_email

# import custom made libraries for controlling the motors
from motor import *

# import library for reading ultrasound sensor
from ultrasound import get_distance

# import keyboard detection
from keyboard_detect import getch
# from raspi_nonblock_key import get_nonblock_key
#name = datetime.now().strftime("%H_%M_on_%Y-%m-%d")

#define motor lag and speed
lag = input('define lag, between 0 to 1: ')
speed = input('speed, between 0.01 and 1: ')
if lag == '':
    lag = 0.1
else:
    lag = float(lag)
if speed == '':
    speed = 0.1
else:
    speed = float(speed)


assert speed >= 0 and speed <= 1

#create empty data string for ultrasound sensor reading. Initialize distance d
data = [0, 0, 0]
wall_dist = 300
'''
# ----------------------------- #
# Do keyboard nonblock get key: Figure out how to make this a module...
import curses
import datetime
stdscr = curses.initscr()
#curses.noecho()
stdscr.nodelay(1) # set getch() non-blocking
stdscr.addstr(0,0,"move using \"asdw\", \"p\" to take picture, \"q\" to exit...")
# ----------------------------- #
'''
# run an infinite loop for the cart. Stops when user presses q or Ctr+C.
while True:
    # Detect keyboard input, see if any key has been pressed. Output is an ord('letterhere')
    # Note: to get back to string format use the chr() function.
    '''
    ch = stdscr.getch()
    if ch == -1:
        ch = 'c'
    else:
        ch = chr(ch)
    '''


    # get distance reading, append to data
    data.append(get_distance())
    # calculate the distance as the average of the last 3 measurements to reduce sensor noise
    wall_dist = (1/3)*(data[-3]+data[-2]+data[-1])
    assert wall_dist > 0 and wall_dist < 10000

    # Problem... loop is getting stuck here. Possible solution, add a time limit, after which
    # it escapes the getch function, and proceeds to scan the rest of the code.
    ch = getch()

    # stop motor if distance to the wall is less than 30cm.
    if wall_dist <= 30:
        if ch.lower() in ['a','s','d','w']:
            ch = []
        # break, then reverse for one second
        stop_motor(1)
        reverse(1)

    elif ch == 'w':
        print('moving forward')
        forward(speed)
        time.sleep(lag)

    # moving backwards
    elif ch == 's':
        print('going backwards')
        reverse(speed)
        time.sleep(lag)

    # turning right
    elif ch == 'd':
        print('turning right')
        right_turn(speed)
        time.sleep(lag)

    elif ch == 'a':
        print('turning left')
        left_turn(speed)
        time.sleep(lag)

    elif ch == 'q':
        print('Exiting remote control')
        break

    # if the camera button has been pressed, take a picture and send an email
    # also activate if p or f have been pressed.
    if camera_switch.pressed_switch() == True or ch == 'p' or ch == 'f':
        name = take_pic_for_email.take_pic()
        send_email.sendpic(name)
        print('picture sent')
        # time.sleep(0.2)
    # reset the ch value.
