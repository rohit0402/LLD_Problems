from enum import Enum

class TableStatus(Enum):
    AVAILABLE="AVAILABLE"
    RESERVED="RESERVED"
    OCCUPIED="OCCUPIED"

class OrderStatus(Enum):
    CREATED="CREATED"
    PREPARING="PREPARING"
    SERVED="SERVED"
    COMPLETED="COMPLETED"

    