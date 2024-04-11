"""
	Elevator 
	Elevator class is used to create car.

	Attribute:
	1) current_floor
	2) direction - up or down
	3) state
"""
import traceback
from time import time
from .request import Request
from .elevator_enum import State, Direction
from sortedcontainers import SortedList

class Elevator:

	def __init__(self):
		self.current_floor = 0
		self.current_state = State.idle.value
		self.current_flow = Direction.up.value
		self.current_jobs = SortedList()
		self.pending_up_jobs = SortedList()
		self.pending_down_jobs = SortedList()

	
	def start_elevator(self):
		while(True):
			if self.check_if_job_exist():
				if self.current_flow == Direction.up.value:
					request = self.current_jobs.pop(0)
					self.process_request(request)
					if not self.current_jobs:
						self.add_pending_down_jobs_to_current_jobs()
				
				# TODO : Add DOWN Logic later;
			else:
				print("Info: No Jobs Found, Elevator Switching to Ideal State...")
				break
	

	def check_if_job_exist(self):
		return True if self.current_jobs else False
	

	def process_request(self, request):
		# Initially at Floor 0th
		start_floor = self.current_floor
		# Firstly pickup User from respective requested floor;
		external_request_floor = request.get_external_request().get_source_floor()
		if start_floor < external_request_floor:
			for i in range(start_floor, external_request_floor+1):
				try:
					time.sleep(1000)
				except Exception as ex:
					print("Something Went Wrong: ", traceback.format_exc())
				print(f"LIFT IS REACHED ON FLOOR : {i}")
				self.current_floor = i
		print(f"Requested Floor Reached: {self.current_floor}, OPENING DOOR")

		# Now Lift will pick one internal request and will drive
		# the elevator to the destination floor and drop user;;
		start_floor = self.current_floor
		internal_request_floor = request.get_internal_request().get_destination_floor()
		if start_floor < internal_request_floor:
			for i in range(start_floor, internal_request_floor+1):
				try:
					time.sleep(1000)
				except Exception as ex:
					print("Something Went Wrong: ", traceback.format_exc())
				print("LIFT IS REACHED ON FLOOR: ", {i})
				self.current_floor = i
				if self.check_new_job_can_be_process():
					break
		print(f"Requested Floor Reached: {self.current_floor}, OPENING DOOR")


	def check_new_job_can_be_process(self, cur_request):
		if self.check_if_job_exist():
			# LIFE IF GOING UP;;
			if self.current_flow == Direction.UP:
				next_request = self.current_jobs.pop(0)
				next_floor = next_request.get_internal_request().get_destination_floor()
				cur_floor = cur_request.get_internal_request().get_destination_floor()
				# If next_requested_floor is coming early before the next destined floor 
				# then re-arrange the current_jobs queue.
				if(next_floor < cur_floor):
					self.current_jobs.add(next_request)
					self.current_jobs.add(cur_request)
					return True
				# Else, just queued the next_request in the current jobs queue;
				self.current_jobs.add(next_request)

			# TODO: LIFE IS GOING DOWN;;
				
		return False



