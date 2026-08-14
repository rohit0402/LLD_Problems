from entities.bill import Bill
from entities.order import Order
from entities.reservation import Reservation
from enums.restaurant_enum import OrderStatus, TableStatus


class RestaurantService:

    def __init__(self):

        self.tables = {}
        self.customers = {}
        self.menu = {}
        self.reservations = {}
        self.orders = {}

    def add_table(self, table):
        self.tables[table.table_id] = table

    def add_customer(self, customer):
        self.customers[
            customer.customer_id
        ] = customer

    def add_menu_item(self, menu_item):
        self.menu[
            menu_item.item_id
        ] = menu_item

    def reserve_table(
        self,
        reservation_id,
        customer_id,
        table_id,
        reservation_time
    ):

        if customer_id not in self.customers:
            raise ValueError("Customer not found")

        if table_id not in self.tables:
            raise ValueError("Table not found")

        table = self.tables[table_id]

        if not table.is_available():
            raise ValueError(
                "Table is not available"
            )

        customer = self.customers[customer_id]

        table.reserve()

        reservation = Reservation(
            reservation_id,
            customer,
            table,
            reservation_time
        )

        self.reservations[
            reservation_id
        ] = reservation

        return reservation

    def seat_customer(self, table_id):

        if table_id not in self.tables:
            raise ValueError("Table not found")

        table = self.tables[table_id]

        table.occupy()

    def create_order(
        self,
        order_id,
        table_id
    ):

        if table_id not in self.tables:
            raise ValueError("Table not found")

        table = self.tables[table_id]

        if table.status != TableStatus.OCCUPIED:
            raise ValueError(
                "Table is not occupied"
            )

        order = Order(
            order_id,
            table
        )

        self.orders[order_id] = order

        return order

    def checkout(self, order_id):

        if order_id not in self.orders:
            raise ValueError("Order not found")

        order = self.orders[order_id]

        bill = Bill(order)

        order.table.release()

        order.update_status(
            OrderStatus.COMPLETED
        )

        return bill