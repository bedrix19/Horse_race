import os
import time
import sys

clear = lambda: os.system('clear')
clear()
print('Cleared')
print('''
   _____,,;;;`;
,~(  )  , )~~\|
' / / --`--,   
 /  \    | '   
''')

def Main():
    print('Welcome to the horse race')

Main()
animation = "|/-\\"
start_time = time.time()
while True:
    for i in range(4):
        time.sleep(0.2)  # Feel free to experiment with the speed here
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    if time.time() - start_time > 10:  # The animation will last for 10 seconds
        break
sys.stdout.write("\rDone!")
