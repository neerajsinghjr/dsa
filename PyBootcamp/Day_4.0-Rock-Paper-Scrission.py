"""
Rock Paper Scrissors is a old style game including key points mentioned below...
1) GAME RULE:
When Two Paper Playing...
    Rock wins against Scissors
    Scissors wins against Papers
    Paper win against Rock

2) GAME PLAY:
User can play with computer by picking options for particular objects for rock, paper, scissor from the respective
option shown on the console screen.
"""

import os
import time
import random

rock = """

     ______
    ,   ____)___
---      ________)   



---



"""

class Player:

    def __init__(self):
        print("")
    def welcome(self) -> str:
        print('Hi, there')
        time.sleep(2)
        print("I'm Roxy")
        time.sleep(2)
        self.playerName = input("What should i call you ?")
        time.sleep(2)


    def loadGame(self) -> None:
        status = print("Press Any Key To Continue or 'q' to exit...")
        if status == 'q|Q|quit|Quit|QUIT':
            return False

        return True


def main():
    playerOne = Player
    playerOne.welcome()
    if playerOne.loadGame():

    else:
        os.system("clear|cls")
        time.sleep(2)
        print("Let's see you again in some time...")
        time.sleep(2)
        print("Roxy Signing off...")
        time.sleep(2)
        print("Bye Bye")


if __name__ == "__main__":
    main()




