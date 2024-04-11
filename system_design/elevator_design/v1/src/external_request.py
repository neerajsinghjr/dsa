"""
	ExternalRequest;
	This request is used to notify the lift about the service 
	call from the service floor.
"""

class ExternalRequest:

	def __init__(self, direction, source_floor):
		self.direction = direction
		self.source_floor = source_floor

	def get_source_floor(self):
		return self.source_floor
	
	def get_direction(self):
		return self.direction
	
	def set_direction(self, direction):
		self.direction = direction

	def set_source_floor(self, source_floor):
		self.source_floor = source_floor

	def get_source_floor(self):
		return self.source_floor