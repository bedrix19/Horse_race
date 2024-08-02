import os
import time
import sys
import threading

from enum import Enum

class Horse(Enum):
    ALBERT  = 'A'
    BELLA   = 'B'
    CASH    = 'C'

class Loader:
    def __init__(self):
        self.stop_loading = False
        self.load_thread = threading.Thread(target=self.loader)

    def loader(self):
        animation = "|/-\\"
        while not self.stop_loading :
            for i in range(4):
                time.sleep(0.2)  # Feel free to experiment with the speed here
                print(f"\r{animation[i % len(animation)]}",end='',flush=True)

    def start(self):
        self.load_thread.start()

    def stop(self):
        self.stop_loading = True
        self.load_thread.join()
        print('\r'+' '*20+'\r',end='')


def Main():
    loader = Loader()
    print('####################### Welcome to the horse race #######################')
    print('Choose your horse:')
    [print(x) for x in [f"[{str(h.value)}] - {str(h.name)}" for h in Horse]]

    loader.start()
    option = input()
    loader.stop()

    match option.upper():
        case 'A':
            print('@')
    print('You choose:',option)

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
'''
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
'''
