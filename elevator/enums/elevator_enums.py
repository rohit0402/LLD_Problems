from enum import Enum

class Direction(Enum):
    UP="UP"
    DOWN="DOWN"
    IDLE="IDLE"

class ElevatorState(Enum):
    IDLE="IDLE"
    MOVING="MOVING"
    DOOR_OPEN="DOOR_OPEN"