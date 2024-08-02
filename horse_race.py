import os
import time
import sys
import threading

from enum import Enum

class Horse(Enum):
    ALBERT  = 'A'
    BELLA   = 'B'
    CASH    = 'C'
    DAKOTA  = 'D'
    ECLIPSE = 'E'

class HorseRace:
    def __init__(self, num_players):
        self.num_players = num_players
        self.players = []

    def add_player(self,name,bet):
        self.players.append((name,bet))

class Loader:
    def __init__(self):
        self.stop_loading = False
        self.load_thread = threading.Thread(target=self.loader)

    def loader(self):
        animation = "|/-\\"
        while not self.stop_loading :
            for i in range(4):
                if self.stop_loading : break
                time.sleep(0.2)  # Feel free to experiment with the speed here
                print(f"\r{animation[i % len(animation)]}",end='',flush=True)

    def start(self):
        self.load_thread.start()

    def stop(self):
        self.stop_loading = True
        self.load_thread.join()
        print('\r'+' '*20+'\r',end='')


def Main():
    print('######################### Welcome to the Horse Race #########################')
    print('''
                    _____,,;;;`;            ;';;;,,_____
                ,~(  )  , )~~\|              |/~~( ,  (  )~,
                ' / / --`--,                    ,--`--\  \ `
                 /  \    | '                    ' |   /   \ 
#############################################################################''')
    try :
        players = int(input('\nEnter the number of glambers: ').strip())
    except ValueError:
        players = 1
    if players < 1 : return

    race = HorseRace(players)

    for i in range(players):
        print(f'Enter the name of gambler {i+1}')
        gambler = input().strip().upper()

        print('Choose your horse:')
        [print(x) for x in [f"[{h.value}] - {h.name}" for h in Horse]]

        loader = Loader()
        loader.start()
        option = input('\r').strip().upper()
        loader.stop()
        sys.stdout.write('\033[F') # cursor up 1 line
        sys.stdout.write('\033[K') # deletes 1 line

        if option not in ['A','B','C','D','E'] : return
        print(f'{gambler} chose {Horse(option).name}')
        race.add_player(gambler, Horse(option))

Main()
