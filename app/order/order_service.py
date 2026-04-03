from app.division.json_manage import Json_Class
from app.menu_manager.item import food_items
from app.logs.logger import write_log


class Order_service:
    def __init__(self):
        self.tables = {}

    def take_order(self):
        try:
            json_obj2 = Json_Class()
            order_data = json_obj2.read_orders()

            if not order_data:
                order_data = {}

            json_obj3 = Json_Class()
            tables = json_obj3.read_table()   

            menu = food_items()  

            table_no = int(input("Enter Table Number: "))

            table_found = False
            customer_name = ""

            for t in tables:
                if t["table_id"] == table_no:
                    customer_name = t["customer_name"]
                    table_found = True
                    break

            if not table_found:
                print("Table is not booked yet")
                return

            print(f"\nOrder for {customer_name} (Table {table_no})")

            order_items = []

            while True:
                item_name = input("Enter Item Name (or 'done' to finish): ").strip().lower()

                if item_name == "done":
                    break

                found_in_menu = False

                for category, items in menu.items():  
                    for name, details in items.items():
                        if name.lower() == item_name:
                            found_in_menu = True

                            size = input("Enter size (half/full): ").strip().lower()
                            if size not in ["half", "full"]:
                                print("Invalid size")
                                continue

                            price = details[f"{size}_plate"]

                            quantity = input("Enter quantity: ")
                            if not quantity.isdigit():
                                print("Invalid quantity")
                                continue

                            quantity = int(quantity)

                            order_items.append({
                                "item": item_name,
                                "size": size,
                                "quantity": quantity,
                                "price": price
                            })

                            print("Item added")
                            break

                if not found_in_menu:
                    print("Item not found in menu")

            if order_items:
                order_data[str(table_no)] = {  
                    "customer_name": customer_name,
                    "items": order_items
                }

                json_obj2.write_orders(order_data)

                print("Order saved successfully")
                # write_log(f"Order saved for table {table_no}")   

            else:
                print("No items ordered")

        except Exception as e:
            print("Error:", e)
            # write_log(f"Error during order: {e}")   

    def update_orders(self):
        try:
            json_obj2 = Json_Class()
            order_data = json_obj2.read_orders()

            table_no = input("Enter Table Number: ").strip()

            if table_no not in order_data:
                print("No order found")
                return

            order = order_data[table_no]

            print("Customer:", order["customer_name"])

            item = order["items"][0]
            print("Current:", item["item"], "x", item["quantity"])

            more = input("Add another item (yes/no): ").lower()

            if more == "yes":
                new_item = input("Enter item name: ")
                size = input("Enter size (half/full): ")
                quantity = input("Enter quantity: ")

                if not quantity.isdigit():
                    print("Invalid quantity")
                    return

                quantity = int(quantity)

                new_data = {
                    "item": new_item,
                    "size": size,
                    "quantity": quantity
                }

                order["items"].append(new_data)
                print("New item added")

            json_obj2.write_orders(order_data)

            print("Order updated successfully")
            # write_log(f"Order updated for table {table_no}")   

        except Exception as e:
            print("Error:", e)
            write_log("Error during update: ",e)   