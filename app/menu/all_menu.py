from app.menu_manager.item import food_items
from app.division.admin_manager import Admin_Menu_manager
from app.division.staff_manager import Staff_Menu_manager
import json

class AdminMenu:

    def show_menu(self):
        try:

            while True:
                print("==========================")
                print(" ****ADMIN MENU**** ")
                print("==========================")
                print("1. view food item ")
                print("2. add food item ")
                print("3. delete food item ")
                print("4. update food item ") 
                print("5. exit")

                choice = input("enter your choice :")
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
                        ob.update_food()

                    elif choice == 4:
                        ob = Admin_Menu_manager()
                        ob.delete_food()

                    elif choice == 5:
                        print("thank you for exit ")
                        break

                    else:
                        print("invalid choice.")

        except Exception as e:
            print(e)

class StaffMenu:

    def show_menu(self):
        try:

            while True:
                print("==========================")
                print(" ****STAFF MENU**** ")
                print("==========================")
                print("1. view food menu ")
                print("2. take order ")
                print("3. table booking" )
                print("4. Update Order ")
                print("5. generate bill")
                print("6. exit")

                choice = input("enter your choice :")
                if choice.isdigit():
                    choice = int(choice)
                    if choice ==1:
                        ob = Staff_Menu_manager()
                        ob.view_menu()

                    elif choice == 2:
                        ob = Staff_Menu_manager()
                        ob.take_order()

                    elif choice == 3:
                        ob = Staff_Menu_manager()
                        ob.table_booking()
                    elif choice == 4:
                        ob = Staff_Menu_manager()
                        ob.update_orders()
                    elif choice == 5:
                        ob = Staff_Menu_manager()
                        ob.generate_bill()

                    else:
                        print("invalid choice. ")

        except Exception as e:
            print(e)

