from app.menu_manager.item import food_items
from app.division.admin_manager import Admin_Menu_manager
from app.division.staff_manager import Staff_Menu_manager
import json

class AdminMenu:

    def show_menu(self):
        try:

            while True:
                print("\033[94m==========================")
                print("\033[92m ****ADMIN MENU**** ")
                print("\033[94m==========================")
                print("1. view food item ")
                print("2. add food item ")
                print("3. delete food item ")
                print("4. update food item ") 
                print("5. exit")

                choice = input("\033[98menter your choice :")
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 1:
                        ob = Admin_Menu_manager()
                        ob.view_food_menu()

                    elif choice == 2:
                        ob = Admin_Menu_manager()
                        ob.add_food()

                    elif choice == 3:
                        ob = Admin_Menu_manager()
                        ob.delete_food()

                    elif choice == 4:
                        ob = Admin_Menu_manager()
                        ob.update_food()

                    elif choice == 5:
                        print("thank you for exit ")
                        break

                    else:
                        print("\033[91invalid choice.")

        except Exception as e:
            print(e)

class StaffMenu:

    def show_menu(self):
        try:

            while True:
                print("\033[94m==========================")
                print("\033[95m ****STAFF MENU**** ")
                print("\033[94m==========================")
                print("1. view food menu ")
                print("2. view tables ")
                print("3. table booking ")
                print("4. take order" )
                print("5. Update Order ")
                print("6. generate bill")
                print("7. exit")

                choice = input("\033[94menter your choice :")
                if choice.isdigit():
                    choice = int(choice)
                    if choice ==1:
                        ob = Staff_Menu_manager()
                        ob.view_food_menu()
                     
                    elif choice == 2:
                        ob = Staff_Menu_manager()
                        ob.view_tables()

                    elif choice == 3:
                        ob = Staff_Menu_manager()
                        ob.table_booking()
                        
                    elif choice == 4:
                        ob = Staff_Menu_manager()
                        ob.take_order()    
                    elif choice == 5:
                        ob = Staff_Menu_manager()
                        ob.update_orders()
                    elif choice == 6:
                        ob = Staff_Menu_manager()
                        ob.generate_bill()

                    else:
                        print("\033[91invalid choice. ")

        except Exception as e:
            print(e)

