"""
	InternalRequest : This request will be placed from inside the 
	elevator car to reach the destination floor.

	Characteristics for InternalRequest
	1) Floor to reach
	2) Direction
"""


class InternalRequest:
	
	def __init__(self, destination_floor):
		self.destination_floor = destination_floor

	def get_destination_floor(self):
		return self.destination_floor

	def set_destination_floor(self, destination_floor):
		self.destination_floor = destination_floor
