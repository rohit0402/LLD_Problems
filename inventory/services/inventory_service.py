from entities.inventory_item import InventoryItem
from entities.inventory_transactions import InventoryTransaction
from enums.inventory_enums import TransactionType

class InventoryService:
    def __init__(self):
        self.inventory={}
        self.transactions={}

    def get_key(self,product_id,warehouse_id):
        return (product_id,warehouse_id)

    def create_inventory(self,product,warehouse):
        key=self.get_key(product.product_id,warehouse.warehouse_id)
        if key in self.inventory:
            raise ValueError("Inventory already exists")

        item=InventoryItem(product,warehouse)
        self.inventory[key]=item
        return item

    def get_inventory(self,product_id,warehouse_id):
        key=self.get_key(product_id,warehouse_id)
        if key not in self.inventory:
            raise ValueError("Inventory not found")

        return self.inventory[key]

    def add_stock(self,transaction_id,product_id,warehouse_id,quantity):
        item=self.get_inventory(product_id,warehouse_id)
        item.add_stock(quantity)
        transaction=InventoryTransaction(transaction_id,TransactionType.STOCK_ADDED,item.product,item.warehouse,quantity)
        self.transactions[transaction_id]=transaction

    def remove_stock(self,transaction_id,product_id,warehouse_id,quantity):
        item=self.get_inventory(product_id,warehouse_id)
        item.remove_stock(quantity)
        transaction=InventoryTransaction(transaction_id,TransactionType.STOCK_REMOVED,item.product,item.warehouse,quantity)
        self.transactions[transaction_id]=transaction

    def reserve_stock(self,transaction_id,product_id,warehouse_id,quantity):
        item=self.get_inventory(product_id,warehouse_id)
        item.reserve(quantity)
        transaction=InventoryTransaction(transaction_id,TransactionType.STOCK_RESERVED,item.product,item.warehouse,quantity)
        self.transactions[transaction_id]=transaction

    def release_stock(self,transaction_id,product_id,warehouse_id,quantity):
        item=self.get_inventory(product_id,warehouse_id)
        item.release(quantity)
        transaction=InventoryTransaction(transaction_id,TransactionType.STOCK_RELEASED,item.product,item.warehouse,quantity)
        self.transactions[transaction_id]=transaction

    def sell_reserved_stock(self,transaction_id,product_id,warehouse_id,quantity):
        item=self.get_inventory(product_id,warehouse_id)
        item.sell_reserved(quantity)
        transaction=InventoryTransaction(transaction_id,TransactionType.STOCK_TRANSFERED,item.product,item.warehouse,quantity)
        self.transactions[transaction_id]=transaction