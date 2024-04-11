from enum import Enum


class Direction(Enum):
	up = 'UP'
	down = 'DOWN'


class State(Enum):
	moving = 'MOVING'
	stop = 'STOP'
	idle = 'IDLE'
	