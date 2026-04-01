from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from app.menu_manager.item import food_items
from app.logs.logger import write_log




class Order_service:
    def __init__(self):
        self.file = Read_mode()
        self.writefile = Write_mode()
        self.tables = {}
         
    def take_order(self):
        data = food_items()
        try:
        
            order_data = self.file.read_file("app/database/orders.json")
            table_data = self.file.read_file("app/database/table.json")
                
            table_no = int(input("\033[97mEnter Table Number: "))
           
            table_found = False
            customer_name = ""
            for t in table_data:
                if t["table_id"] == table_no :
                    customer_name = t["customer_name"]
                    table_found = True
                    break
            if not table_found:
                print("\033[91m Table is not booked yet")
                return

            print(f"\nOrder for {customer_name} (Table {table_no})")

            order_items = []   

            while True:
                item_name = input("Enter Item Name (or 'done' to finish): ").strip().lower()

                if item_name == "done":
                    break

                found_in_menu = False

                for category, items in data.items():
                    for name, details in items.items():
                        if name.lower() == item_name.lower():
                            found_in_menu = True
                            
                            size = input("\033[94mEnter size (half/full): ").strip().lower()
                            if size not in ["half", "full"]:
                                print("Invalid size")
                                break
                            price = details[f"{size}_plate"]

                            quantity = input("\033[98mEnter quantity: ")
                            if not quantity.isdigit():
                                print("\033[91m invalid quantity ")
                                return
                            
                            quantity = int(quantity)
        
                            order_items.append({
                                "item": item_name,
                                "size": size,
                                "quantity": quantity,
                                "price": price
                            })
                            print("Item added ")
                            
                            break
                if not found_in_menu:
                    print("\033[91m Item not found in menu. Try again.")
            if order_items:

                order_data[table_no] = {
                    "customer_name": customer_name,
                    "items": order_items
                }

                self.writefile.write_file("app/database/orders.json", order_data)

                print("\033[92mOrder saved successfully ")
                write_log("order save successfully : ")
                    
            else:
                print("No items ordered")

        except Exception as e:
            print("Error:", e)
            
    def update_orders(self):
        try:
            data = self.file.read_file("app/database/orders.json")
            table_no = input("Enter Table Number: ").strip()

            if table_no not in data:
                print("No order found")
                return

            order = data[table_no]

            print("Customer:", order["customer_name"])

            item = order["items"][0]

            print("Current:", item["item"], "x", item["quantity"])

            more = input("\033[92madd another item (yes/no): ").lower()

            if more == "yes":
                new_item = input("\033[93m Enter item name: ")
                size = input("\033[93m Enter size (half/full): ")
                quantity = input("\033[93m Enter quantity: ")
                if not quantity.isdigit():
                    print("\033[91m invalid quantity ")
                    return
               

                new_data = {
                    "item": new_item,
                    "size": size,
                    "quantity": quantity
                }

                order["items"].append(new_data)
                print("\033[92m New item added ")

            self.writefile.write_file("app/database/orders.json", data)

            print("\033[92m Order updated successfully ")
            write_log("order updated successfully table no  :" ,table_no)

        except Exception as e:
            print("Error:",e)
            
    