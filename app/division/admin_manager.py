from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from app.logs.logger import write_log

class Admin_Menu_manager:
    def __init__(self):
        self.food_list = []
        self.file = Read_mode()
        self.writefile = Write_mode()
     
    def view_food_menu(self):
        try:
            data = self.file.read_file("app/database/item_data.json")
            print("\n\033[94m ==============================================")
            print("\033[92m ********* Velvet Valley Restaurant ********* ")
            print("\033[94m=================================================\033[94m")
            print(" \033[92m          RESTAURANT FOOD MENU")
            print("\n\033[94m=================================\033[94m")
            
            for category, items in data.items():
                
                
                print("\033[95m|=========================================================|\033[0m")
                print(f"\n\033[96m                     {category}                        ")
                print("\033[95m|=========================================================|\033[0m")
                for name, price in items.items():

                    half = price[" half_plate"]
                    full = price[" full_plate"]
                    
                    print(f"\033[96m |   {name:<25} | Half: ₹{half:<5}|  Full: ₹{full}  |\033[0m")
                    
        except Exception as e:
            print(e)
    def add_food(self):
        data = self.file.read_file("app/database/item_data.json")
    
        try:
            while True:

                category = input("\033[93m enter category: ").title()
                name = input("\033[93m enter food name: ").title()
                half = int(input("\033[93m enter half plate price: "))
                full = int(input("\033[93m enter full plate price: "))

                if category not in data:
                    data[category] = {}

                data[category][name] = {
                "half_plate": half,
                "full_plate": full}  

                print("\033[92mfood added successfully")
               
                write_log(f"Food add: {name} ({category})")

                choice = input("\033[96m add more food? (yes/no): ")

                if choice.lower() != "yes":
                    break
            self.writefile.write_file("app/database/item_data.json", data)
           
        except Exception as e:
            print(e)
    
    def update_food(self):
        try:
            data = self.file.read_file("app/database/item_data.json")
            
            category = input("\033[93m enter category: ").title()
            food_name = input("\033[93m enter food name to update: ").title()
            if category in data and food_name in data[category]:

                half = int(input("\033[93m enter new half plate price: "))
                full = int(input("\033[93m enter new full plate price: "))

                data[category][food_name]["half_plate"] = half
                data[category][food_name]["full_plate"] = full

                self.writefile.write_file("app/database/item_data.json", data)
            
                print("\033[98mfood updated successfully")
                write_log("food updated successfully :"+ food_name)
            else:    
                print("\033[91m food not found\033[98m")
                write_log("food not found"+food_name)
        except Exception as e:
            print(e)
                    

    def delete_food(self):
        try:
            data = self.file.read_file("app/database/item_data.json")

            category = input("\033[93m enter category: ").strip().lower()
            name = input("\033[93m please enter food name to delete: ").strip().lower()

            if category in data and name in data[category]:

                data[category].pop(name)
                print("\033[92mfood deleted successfully")
                write_log("food deleted successfully :"+ category,name)
                self.writefile.write_file("app/database/item_data.json", data)

            else:
                print("\033[91m food not found")
                write_log("food not found"+category, name)

        except Exception as e:
            print(e)
            
        
        
   
            
            