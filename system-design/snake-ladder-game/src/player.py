"""
	Player:
	
	This class is used to store the details of player.

"""


class Player:

	def __init__(self, id, name, email=None, gender=None):
		self.id = id
		self.name = name
		self.email = email
		self.gender = gender

	def get_by_player_id(self):
		return self.id 