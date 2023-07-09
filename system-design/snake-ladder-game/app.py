"""
	APP Run
"""

from src.dice import Dice 
from src.jumper import Jumper
from src.player import Player 
from src.playground import Playground
from collections import deque

if __name__ == '__main__':
	# Player init
	player1 = Player(1, 'Devil')
	player2 = Player(2, 'Lucifer')
	player3 = Player(3, 'Lamia')
	players = deque([player1, player2, player3])
	# Snakes init
	snake1 = Jumper(99, 50)
	snake2 = Jumper(80, 30)
	snake3 = Jumper(40, 10)
	snakes = deque([snake1, snake2, snake3])
	# Ladder init
	ladder1 = Jumper(40, 10)
	ladder2 = Jumper(60, 40)
	ladder3 = Jumper(55, 30)
	ladders = deque([ladder1, ladder2, ladder3])
	# Dice init
	dice = Dice(2)
	# Player position
	player_position = {1: 0, 2:0, 3:0}
	# boardsize init
	boardsize = 100
	pg = Playground(players, dice, snakes, ladders, boardsize, player_position)
	pg.game_start()
	print("Game End!")