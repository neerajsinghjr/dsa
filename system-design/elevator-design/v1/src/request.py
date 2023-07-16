"""
	Request: Request container is used to encapsulate 
	InternalRequest container and ExternalRequest
	container.
"""

class Request:

	def __init__(self, internal_request, external_request):
		self.internal_request = internal_request
		self.external_request = external_request

	def get_internal_request(self):
		return self.internal_request

	def set_internal_request(self, new_request):
		self.internal_reqeust = new_request

	def get_external_request(self):
		return self.external_request

	def set_external_request(self, new_request):
		self.external_request = new_request
