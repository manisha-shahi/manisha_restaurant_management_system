from app.auth.login import Info
from app.auth.signup import Registration

class Manage_Menu:
    def Manage(self):
        try:

            while True:
                print("\033[94m========================================\033[94m")
                print("\033[92m ********* Velvet Valley Restaurant ********* ")
                print("\033[94m========================================\033[94m")
                print("\033[92m *******registration*******\033[92m")
                print("\033[91m 1. signup ")
                print("\033[91m 2. login ")
                print("\033[91m 3. exit ")

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
                        print("\033[97mthank you for registration")
                        break
                    else:
                        print("\033[98minvalid choice")

        except Exception as e:
            print(e)

