from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from app.file_handler.append_mode import Append_mode
from app.menu_manager.item import food_items
from datetime import datetime
import json 

class Staff_Menu_manager:

    def __init__(self):
        self.file = Read_mode()
        self.writefile = Write_mode()
        self.tables = {}
    
    def view_food_menu(self):
        try:
            data = self.file.read_file("app/database/item_data.json")
            print("\n\033[94m ==============================================")
            print("\033[92m ********* Velvet Valley Restaurant ********* ")
            print("\033[94m=================================================\033[94m")
            print(" \033[92m          RESTAURANT FOOD MENU")
            print("\n\033[94m=================================\033[94m")

            for category, items in data.items():

                print(f"\n\033[96m---- {category} ----")

                for name, price in items.items():

                    half = price["half_plate"]
                    full = price["full_plate"]

                    print(f"{name:<25}  Half: ₹{half:<5}  Full: ₹{full}")
        except Exception as e:
            print("Error:",e)

    def view_tables(self):
        try:
            data = self.file.read_file("app/database/table.json")

            print("\n===== TABLE DETAILS =====\n")

            for table in data:
                print("Table ID:", table["table_id"])
                print("Capacity:", table["capacity"])
                print("Status:", table["status"])

        
        except Exception as e:
            print("Error:", e)

    def table_booking(self):

        try:
            data = self.file.read_file("app/database/table.json")
            
            customer_name = input("\033[93mEnter customer name: ").strip().lower()
            people = int(input("Enter number of people: "))
            table_no = int(input("\nEnter table number to book: "))
            date = input("Enter booking date (DD-MM-YYYY): ")
            time = input("Enter booking time (HH:MM): ")

            booking_time = f"{date} {time}"
            
            found = False

            for table in data:
                if table["table_id"] == table_no:
                    found = True
                    if table["status"] == "available" and table["capacity"] >= people:
                        table["status"] = "booked"
                        table["booking_time"] = booking_time  
                        table["customer_name"] = customer_name   
                        print(f"Table {table_no} booked successfully ")
                        print("Customer Name:", customer_name)
                        print("Booking Time:", booking_time)

                        self.writefile.write_file("app/database/table.json", data)
                        break

                    elif table["status"] == "available" and table["capacity"] < people:
                        print("Table capacity is not enough, trying other tables")

                        count = 0

                        for n in data:
                            if n["status"] == "available":
                                count += n["capacity"]

                                n["status"] = "booked"
                                n["booking_time"] = booking_time
                                n["customer_name"] = customer_name

                                print(f"Table {n['table_id']} booked")

                                if count >= people:
                                    break

                        if count >= people:
                            self.writefile.write_file("app/database/table.json", data)
                        else:
                            print("Not enough tables are available")

                        break

                    else:
                        print("Table already booked")
                        break

            if not found:
                print("Table not found")
        
        except Exception as e:
            print("Error:",e)
    def take_order(self):
        data = food_items()
        try:
        
                order_data = self.file.read_file("app/database/orders.json")
                
                table_no = input("\033[97mEnter Table Number: ").strip()
                table_data = self.file.read_file("app/database/table.json")
                table_found = False
                customer_name = ""
                for t in table_data:
                    if str(t["table_id"]) == table_no and t["status"] == "booked":
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
                                    print("invalid quantity ")
                                    break
        
                                order_items.append({
                                    "item": item_name,
                                    "size": size,
                                    "quantity": quantity,
                                    "price": price
                                })
                                print("Item added ")
                                break
                    if not found_in_menu:
                        print("Item not found in menu. Try again.")
                if order_items:

                    order_data[table_no] = {
                        "customer_name": customer_name,
                        "items": order_items
                    }

                    self.writefile.write_file("app/database/orders.json", order_data)

                    print("Order saved successfully ")
                    
                else:
                    print("No items ordered")

        except Exception as e:
            print("Error:", e)
    def update_orders(self):
        try:
            order_data = self.file.read_file("app/database/orders.json")
            table_no = input("Enter Table Number to update: ").strip()

            if table_no not in self.tables:
                print("No order found for this table")
                return

            order_data = self.tables[table_no]
            order_items = order_data["items"]

            print("\nTable", table_no, "Order:")

            i = 1
            for item in order_items:
                print(i, item["item"], item["size"], "x", item["quantity"])
                i += 1

            choice = input("Enter item number: ")

            if not choice.isdigit():
                print("Invalid input")
                return

            choice = int(choice) - 1

            if choice < 0 or choice >= len(order_items):
                print("Invalid item number")
                return

            action = input("Enter 'u' to update or 'd' to delete: ").lower()

        
            if action == "u":
                new_qty = input("Enter new quantity: ")

                if not new_qty.isdigit():
                    print("Invalid quantity")
                    return

                order_items[choice]["quantity"] = int(new_qty)
                print("Quantity updated successfully")

            elif action == "d":
                removed_item = order_items.pop(choice)
                print(removed_item["item"], "removed successfully")
                
            else:
                print("Invalid action")
                return

            if len(order_items) == 0:
                del self.tables[table_no]
                print("All items removed. Table order deleted.")
            else:
                self.tables[table_no]["items"] = order_items
                
            self.writefile.write_file("app/database/orders.json", order_data)

            print("Order updated successfully ")
        except Exception as e:
            print("Error:", e)

    def generate_bill(self):
        try:

            table_no = input("\033[94mEnter Table Number for Bill: ").strip()
            if table_no not in self.tables:
                print("No order found for this table.")
                return

            order_items = tables[table_no]
            total = 0
            print(f"\n\033[99m======= BILL for Table {table_no} =======")
            for item in order_items:
                if "size" in item:
                    print(f"{item['item']} ({item['size']}): {item['quantity']} x ₹{item['price']} = ₹{item['quantity']*item['price']}")
                else:
                    print(f"{item['item']}: {item['quantity']} x ₹{item['price']} = ₹{item['quantity']*item['price']}")
                total += item['quantity']*item['price']

            print(f"Total: ₹{total}")
            print("\033[96m==============================\n")
            del tables[table_no]
            print("Order cleared after billing \n")
        except Exception as e:
            print("Error:",e)