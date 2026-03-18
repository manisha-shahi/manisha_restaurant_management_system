from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from app.file_handler.append_mode import Append_mode
from app.menu_manager.item import food_items
import json 

class Staff_Menu_manager:

    def __init__(self):
        self.file = Read_mode()
        self.writefile = Write_mode()
        self.orders = []
        self.tables = {}

    def view_menu(self):
        print("\n======= MENU =======")

        data = food_items()

        for category, items in data.items():
            print(f"\n--- {category} ---")

            for item, price in items.items():
                if "half_plate" in price:   
                    print(f"{item}: Half ₹{price['half_plate']} / Full ₹{price['full_plate']}")
                else:
                    print(f"{item}: ₹{price['price']}")

        print("===================\n")
    def take_order(self):
        data = food_items()

        table_no = input("Enter Table Number: ").strip()
        order_items = []

        while True:
            item_name = input("Enter Item Name (or 'done' to finish): ").strip()

            if item_name.lower() == "done":
                break

            found = False

            for category, items in data.items():
                if item_name in items:
                    found = True
                    if "half_plate" in items[item_name]:
                        size = input("Enter size (half/full): ").strip().lower()

                        if size not in ["half", "full"]:
                            print("Invalid size")
                            continue

                        quantity = int(input("Enter quantity: "))

                        order_items.append({
                            "item": item_name,
                            "size": size,
                            "quantity": quantity,
                            "price": items[item_name][f"{size}_plate"]
                        })

            if not found:
                print("Item not found in menu. Try again.")

        if not order_items:
            print("No items ordered.")
            return

        self.tables[table_no] = order_items
        print(f"Order added for Table {table_no} ")
    def table_booking(self):

        table_no = input("Enter Table Number to book: ").strip()
        if table_no in tables:
            print(f"Table {table_no} already has an order!")
        else:
            print(f"Table {table_no} booked successfully ")
            tables[table_no] = []

    def update_order(self):
        table_no = input("Enter Table Number to update: ").strip()

        if table_no not in self.tables:
            print("No order found for this table ")
            return

        order_items = self.tables[table_no]

        print("\nCurrent Order:")
        for i, item in enumerate(order_items, start=1):
            if "size" in item:
                print(f"{i}. {item['item']} ({item['size']}) x {item['quantity']}")
            else:
                print(f"{i}. {item['item']} x {item['quantity']}")

        choice = input("\nEnter item number to update/delete: ")

        if not choice.isdigit():
            print("Invalid choice")
            return

        choice = int(choice) - 1

        if choice < 0 or choice >= len(order_items):
            print("Invalid item number")
            return

        action = input("Enter 'u' to update quantity or 'd' to delete item: ").lower()

        if action == "u":
            new_qty = int(input("Enter new quantity: "))
            order_items[choice]["quantity"] = new_qty
            print("Quantity updated ")

        elif action == "d":
            removed = order_items.pop(choice)
            print(f"{removed['item']} removed ")

        else:
            print("Invalid action")

        self.tables[table_no] = order_items

    
    def generate_bill(self):
        table_no = input("Enter Table Number for Bill: ").strip()
        if table_no not in tables:
            print("No order found for this table.")
            return

        order_items = tables[table_no]
        total = 0
        print(f"\n======= BILL for Table {table_no} =======")
        for item in order_items:
            if "size" in item:
                print(f"{item['item']} ({item['size']}): {item['quantity']} x ₹{item['price']} = ₹{item['quantity']*item['price']}")
            else:
                print(f"{item['item']}: {item['quantity']} x ₹{item['price']} = ₹{item['quantity']*item['price']}")
            total += item['quantity']*item['price']

        print(f"Total: ₹{total}")
        print("==============================\n")
        del tables[table_no]
        print("Order cleared after billing \n")