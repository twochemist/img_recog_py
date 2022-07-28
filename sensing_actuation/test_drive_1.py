'''
First course for the self driving pi. Developed by Fidel Esquivel Estay (PhiDeltaEE)
The purpose of this test drive is to verify the proper functionality of the 4 DC motors
connected to the pi, as well as their handling of motion on the ground. 
'''

# import the motor controlling functions developed 
from motor import *

forward(1.5)
time.sleep(1)

# Go backwards
reverse(1.5)
time.sleep(1)

#turn left
left_turn(0.5)
time.sleep(1)

# move forward
forward(1)
time.sleep(1)

#turn right
right_turn(0.5)
time.sleep(1)