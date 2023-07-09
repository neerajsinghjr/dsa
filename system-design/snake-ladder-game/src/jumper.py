"""
	Jumper:
	Jumper is used to drag down a player from its position 
	to the tail of the snake.

	It will be used by snakes and ladders as well.

	case 1: for snakes
	Player will drag down from top to bottom 

	case 2: for ladder
	Player will climb up from bottom to top
"""

class Jumper:

	def __init__(self, start, end):
		self.start = start
		self.end = end
