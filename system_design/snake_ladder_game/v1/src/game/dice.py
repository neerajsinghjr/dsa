"""
	Dice :
	This class is used to generate and roll the dice 
	over the board.
"""
from random import randint

class Dice:

	def __init__(self, dice_count):
		self.dice_count = dice_count


	def roll_dice(self):
		# lower bound is 1 of single dice;;
		# upper bound is 6 of single dice;;
		lower_bound = self.dice_count * 1
		upper_bound = self.dice_count * 6
		return randint(lower_bound, upper_bound)