
from app.division.json_manage import Json_Class
from app.logs.logger import write_log

class Admin_Menu_manager:
    def __init__(self):
        self.food_list = []
     
    def view_food_menu(self):
        try:
            json_obj5 = Json_Class()
            item_data = json_obj5.read_item()
           
            print("\n\033[94m ==============================================")
            print("\033[92m ********* Velvet Valley Restaurant ********* ")
            print("\033[94m=================================================\033[94m")
            print(" \033[92m          RESTAURANT FOOD MENU")
            print("\n\033[94m=================================\033[94m")
            
            for category, items in item_data.items():
                
                
                print("\033[95m|=========================================================|\033[0m")
                print(f"\n\033[96m                     {category}                        ")
                print("\033[95m|=========================================================|\033[0m")
                for name, price in items.items():

                    half = price["half_plate"]
                    full = price["full_plate"]
                    
                    print(f"\033[96m |   {name:<25} | Half: ₹{half:<5}|  Full: ₹{full}  |\033[0m")
                    
        except Exception as e:
            print("Error:",e)
            write_log("ERROR", "Error during signup: ",e)
    def add_food(self):
        
        json_obj5 = Json_Class()
        item_data = json_obj5.read_item()
        try:
            while True:

                category = input("\033[93m enter category: ").title()
                name = input("\033[93m enter food name: ").title()
                half = int(input("\033[93m enter half plate price: "))
                full = int(input("\033[93m enter full plate price: "))

                if category not in item_data:
                    item_data[category] = {}

                item_data[category][name] = {
                "half_plate": half,
                "full_plate": full
                }  

                print("\033[92mfood added successfully")
                json_obj5.write_item(item_data)
              
                choice = input("\033[96m add more food? (yes/no): ")
                
                if choice.lower() != "yes":
                    break
            
        except Exception as e:
            print("Error:",e)
            write_log("ERROR", "Error during signup: ",e)
    
    def update_food(self):
        try:
            json_obj5 = Json_Class()
            item_data = json_obj5.read_item()
           
            category = input("\033[93m enter category: ").title()
            food_name = input("\033[93m enter food name to update: ").title()
            if category in item_data and food_name in item_data[category]:

                half = int(input("\033[93m enter new half plate price: "))
                full = int(input("\033[93m enter new full plate price: "))

                item_data[category][food_name]["half_plate"] = half
                item_data[category][food_name]["full_plate"] = full
                json_obj5.write_item(item_data)
            
                print("\033[98mfood updated successfully")
                write_log("food updated successfully :", food_name)
            else:    
                print("\033[91m food not found\033[98m")
                write_log("food not found",food_name)
        except Exception as e:
            print("Error:",e)      
            write_log("ERROR", "Error during signup: ",e)
    def delete_food(self):
        try:
            
            json_obj5 = Json_Class()
            item_data = json_obj5.read_item()

            category = input("\033[93m enter category: ").strip().lower()
            name = input("\033[93m please enter food name to delete: ").strip().lower()

            if category in item_data and name in item_data[category]:

                item_data[category].pop(name)
                print("\033[92mfood deleted successfully")
                write_log("food deleted successfully :", category,name)
                json_obj5.write_item(item_data)

            else:
                print("\033[91m food not found")

        except Exception as e:
            print("Error:",e)
            write_log("ERROR", "Error during signup: ",e)
            
        
        
   
            
            