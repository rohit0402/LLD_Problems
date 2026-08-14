from entities.product import Product
from entities.warehouse import Warehouse

from services.inventory_service import (
    InventoryService
)


# -----------------------------------------
# Create Product
# -----------------------------------------

laptop = Product(
    "P1",
    "Laptop",
    50000
)


# -----------------------------------------
# Create Warehouses
# -----------------------------------------

mumbai = Warehouse(
    "W1",
    "Mumbai Warehouse"
)

delhi = Warehouse(
    "W2",
    "Delhi Warehouse"
)


# -----------------------------------------
# Inventory Service
# -----------------------------------------

inventory_service = InventoryService()


# -----------------------------------------
# Create Inventory
# -----------------------------------------

mumbai_inventory = (
    inventory_service.create_inventory(
        laptop,
        mumbai
    )
)

delhi_inventory = (
    inventory_service.create_inventory(
        laptop,
        delhi
    )
)


# -----------------------------------------
# Add Stock
# -----------------------------------------

inventory_service.add_stock(
    "TXN1",
    "P1",
    "W1",
    100
)

inventory_service.add_stock(
    "TXN2",
    "P1",
    "W2",
    50
)


print(
    "Mumbai:",
    mumbai_inventory.available_quantity
)

print(
    "Delhi:",
    delhi_inventory.available_quantity
)


# -----------------------------------------
# Reserve Stock
# -----------------------------------------

inventory_service.reserve_stock(
    "TXN3",
    "P1",
    "W1",
    20
)


print(
    "Mumbai available:",
    mumbai_inventory.available_quantity
)

print(
    "Mumbai reserved:",
    mumbai_inventory.reserved_quantity
)


# -----------------------------------------
# Release Reservation
# -----------------------------------------

inventory_service.release_stock(
    "TXN4",
    "P1",
    "W1",
    5
)


print(
    "Mumbai available:",
    mumbai_inventory.available_quantity
)

print(
    "Mumbai reserved:",
    mumbai_inventory.reserved_quantity
)


# -----------------------------------------
# Complete Sale
# -----------------------------------------

inventory_service.sell_reserved_stock(
    "TXN5",
    "P1",
    "W1",
    15
)


print(
    "Mumbai available:",
    mumbai_inventory.available_quantity
)

print(
    "Mumbai reserved:",
    mumbai_inventory.reserved_quantity
)

print(
    "Mumbai total:",
    mumbai_inventory.total_quantity
)