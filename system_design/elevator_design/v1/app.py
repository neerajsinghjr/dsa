from src.elevator import Elevator
from src.request import Request
from src.elevator_enum import State, Direction
from src.internal_request import InternalRequest
from src.external_request import ExternalRequest


if __name__ == '__main__':
	lift_1 = Elevator()
	print(">>>>>>>>>>>. lift : ", lift_1)
	ext_req = ExternalRequest(Direction.up.value, 3)
	print(">>>>>>>>>>>. ext_req: ", ext_req)
	int_req = InternalRequest(10)
	print(">>>>>>>>>>>. int_req: ", int_req)
	request = Request(int_req, ext_req)
	print(">>>>>>>>>>>. req: ", request)
	lift_1.start_elevator()
	
