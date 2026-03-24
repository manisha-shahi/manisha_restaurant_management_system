from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from app.file_handler.append_mode import Append_mode
from app.menu_manager.item import food_items
import json 
class Admin_Menu_manager:
    def __init__(self):
        self.food_list = []
        self.file = Read_mode()
        self.writefile = Write_mode()
        self.appendfile = Append_mode()
     
    def view_food_menu(self):
        try:
            data = self.file.read_file("app/database/item_data.json")
            print("\n\033[94m ==============================================")
            print("\033[92m ********* Velvet Valley Restaurant ********* ")
            print("\033[94m=================================================\033[94m")
            print(" \033[92m          RESTAURANT FOOD MENU")
            print("\n\033[94m=================================\033[94m")

            for category, items in data.items():

                print(f"\n\033[96m===== {category} =====")

                for name, price in items.items():

                    half = price["half_plate"]
                    full = price["full_plate"]

                    print(f"{name:<25}  Half: ₹{half:<5}  Full: ₹{full}")
        except Exception as e:
            print(e)
    def add_food(self):
        data = self.file.read_file("app/database/item_data.json")
    
        try:
            while True:

                category = input("\033[96menter category: ").strip().lower()
                name = input("enter food name: ").strip().lower()
                half = int(input("enter half plate price: "))
                full = int(input("enter full plate price: "))

                if category not in data:
                    data[category] = {}

                data[category][name] = {
                "half_plate": half,
                "full_plate": full} 

                print("\033[92mfood added successfully")
                choice = input("\033[96madd more food? (yes/no): ")

                if choice.lower() != "yes":
                    break
            self.writefile.write_file("app/database/item_data.json", data)
           
        except Exception as e:
            print(e)
    
    def update_food(self):
        try:
            data = self.file.read_file("app/database/item_data.json")
            
            category = input("enter category: ").strip().lower()
            food_name = input("enter food name to update: ").strip().lower()
            if category in data and food_name in data[category]:

                half = int(input("enter new half plate price: "))
                full = int(input("enter new full plate price: "))

                data[category][food_name]["half_plate"] = half
                data[category][food_name]["full_plate"] = full

                self.writefile.write_file("app/database/item_data.json", data)
            
                print("\033[98mfood updated successfully")
            else:    
                print("food not found\033[98m")
        except Exception as e:
            print(e)
                   

    def delete_food(self):
        try:
            data = self.file.read_file("app/database/item_data.json")

            category = input("\033[97menter category: ").strip().lower()
            name = input("please enter food name to delete: ").strip().lower()

            if category in data and name in data[category]:

                data[category].pop(name)
                print("food deleted successfully")
                self.writefile.write_file("app/database/item_data.json", data)

            else:
                print("food not found")

        except Exception as e:
            print(e)