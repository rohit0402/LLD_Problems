from datetime import datetime
from services.restaurant_service import RestaurantService
from entities.table import Table
from entities.menu_item import MenuItem
from entities.customer import Customer
from entities.bill import Bill
from entities.order import Order
restaurant = RestaurantService()

# Table
table1 = Table("T1", 10)
table2 = Table("T2", 10)

restaurant.add_table(table1)
restaurant.add_table(table2)

# Customer
customer1 = Customer(
    "C1",
    "Rohit"
)

restaurant.add_customer(customer1)



# Menu
pizza=MenuItem("M1","Pizza",10)
coffee=MenuItem("M2","Coffee",5)

restaurant.add_menu_item(pizza)
restaurant.add_menu_item(coffee)

# Reservation
reservation=  restaurant.reserve_table(
    "R1","C1","T1",datetime.now()
)

print(f"Reservation ID: {reservation.reservation_id}")

#seat customer
restaurant.tables["T1"].occupy()
print(f"Table {table1.table_id} is occupied")

#create order
order=restaurant.create_order("O1","T1")
order.add_item(pizza,1)
order.add_item(coffee,1)

#checkout
bill=restaurant.checkout("O1")
print(f"Bill: {bill.subtotal}")
print(f"Tax: {bill.tax:.2f}")
print(f"Total: {bill.total:.2f}")