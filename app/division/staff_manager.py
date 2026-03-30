from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode


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
