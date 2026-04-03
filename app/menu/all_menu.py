
from app.division.admin_manager import Admin_Menu_manager
from app.division.staff_manager import Staff_Menu_manager
from app.booking.booking_service import Booking_service
from app.order.order_service import Order_service
from app.billing.billing_service import Billing_service
from app.reports.report_menu import Reportmenu
from app.logs.logger import write_log



class AdminMenu:

    def show_menu(self):
        try:

            while True:
                print("\033[94m==========================")
                print("\033[92m ****ADMIN MENU**** ")
                print("\033[94m==========================")
                print("1. View Food Item ")
                print("2. Add Food Item ")
                print("3. Delete Food Item ")
                print("4. Update Food Item ") 
                print("5. Reports ")
                print("6. Exit")

                choice = input("\033[98m Enter your choice :")
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
                        ob = Reportmenu()
                        ob.menu()
                    elif choice == 6:
                        print("thank you for exit ")
                        break
                    else:
                        print("\033[91m Invalid choice.")

        except Exception as e:
            print("Error:",e)
            write_log("ERROR", "Error during signup: ",e)

class StaffMenu:

    def show_menu(self):
        try:

            while True:
                print("\033[94m==========================")
                print("\033[95m ****STAFF MENU**** ")
                print("\033[94m==========================")
                print("1. View Food Menu ")
                print("2. View Tables ")
                print("3. Table Booking ")
                print("4. Take Order" )
                print("5. Update Order ")
                print("6. Generate Bill")
                print("7. Exit")

                choice = input("\033[94m Enter your choice :")
                if choice.isdigit():
                    choice = int(choice)
                    if choice ==1:
                        ob = Staff_Menu_manager()
                        ob.view_food_menu()
                     
                    elif choice == 2:
                        ob = Staff_Menu_manager()
                        ob.view_tables()

                    elif choice == 3:
                        ob = Booking_service()
                        ob.table_booking()
                        
                    elif choice == 4:
                        ob = Order_service ()
                        ob.take_order()    
                    elif choice == 5:
                        ob = Order_service ()
                        ob.update_orders()
                    elif choice == 6:
                        ob = Billing_service()
                        ob.generate_bill()
                    elif choice == 7:
                        print("thank you for exit ")
                        break
                    else:
                        print("\033[91m Invalid choice. ")

        except Exception as e:
            print("Error:",e)
            write_log("ERROR", "Error during signup: ",e)

