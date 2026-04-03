from app.logs.logger import write_log
from app.division.json_manage import Json_Class

class Staff_Menu_manager:

    def __init__(self):
        self.tables = {}
    
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

                print(f"\n\033[96m---- {category} ----")

                for name, price in items.items():

                    half = price["half_plate"]
                    full = price["full_plate"]

                    print(f"{name:<25}  Half: ₹{half:<5}  Full: ₹{full}")
        except Exception as e:
            print("Error:",e)
            write_log("ERROR", f"Error during signup: {e}")

    def view_tables(self):
        try:
            json_obj3 = Json_Class()
            data = json_obj3.read_table()

            print("\n===== TABLE DETAILS =====\n")

            for table in data:
                print("Table ID:", table["table_id"])
                print("Capacity:", table["capacity"])
                print("Status:", table["status"])

        
        except Exception as e:
            print("Error:", e)
            write_log("ERROR", f"Error during signup: {e}")
