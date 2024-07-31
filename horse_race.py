import os
import time
import sys

from enum import Enum

class Horse(Enum):
    ALBERT  = 'A'
    BELLA   = 'B'
    CASH    = 'C'


def Main():
    print('####################### Welcome to the horse race #######################')
    print('Choose your horse:')
    print([h.value for h in Horse])

Main()

#clear = lambda: os.system('clear')
#clear()
#print('Cleared')
#print('''
#   _____,,;;;`;
#,~(  )  , )~~\|
#' / / --`--,   
# /  \    | '   
#''')

#         -~~,
#  ,; _ _~ |\|
# ;; ( )_, )
# ;; /|  |.\

animation = "|/-\\"
start_time = time.time()
while True:
    for i in range(4):
        time.sleep(0.2)  # Feel free to experiment with the speed here
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 5:  # The animation will last for 5 seconds
        break
sys.stdout.write("\rDone!\n")
