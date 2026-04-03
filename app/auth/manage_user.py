from app.auth.login import Info
from app.auth.signup import Registration
from app.logs.logger import write_log

class Manage_Menu:
    def Manage(self):
        try:

            while True:
                print("\033[94m========================================\033[94m")
                print("\033[92m ********* Velvet Valley Restaurant ********* ")
                print("\033[94m========================================\033[94m")
                print("\033[92m *******Registration*******\033[92m")
                print("\033[91m 1. SIGNUP ")
                print("\033[91m 2. LOGIN  ")
                print("\033[91m 3. EXIT ")

                choice = input("\033[96mplease enter your choice :")
                if choice.isdigit():
                    choice = int(choice)
                    if choice == 1:
                        ob = Registration()
                        ob.signup()
                    elif choice == 2:
                        ob = Info()
                        ob.Login()
                    elif choice == 3:
                        print("\033[97m Thank you for registration")
                        break
                    else:
                        print("\033[91m Invalid choice")

        except Exception as e:
            print("Error:",e)
            write_log("ERROR", f"Error during signup: {e}")

