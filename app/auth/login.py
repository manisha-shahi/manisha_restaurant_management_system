from app.file_handler.read_mode import Read_mode
from app.menu.all_menu import AdminMenu, StaffMenu
from getpass import getpass

import json 
class Info: 
    def __init__(self):
        self.file = Read_mode()

    
    def Login(self):
        listdata = self.file.read_file("app/database/user.json")
        try:

            username = input("\033[91mplease enter your name :")
            password = getpass("please enter your password:")
            role = input("please enter your role admin/staff :")

            for data in listdata:
                if( username == data["username"] and password == data["password"] and role == data["role"].lower()):
                    print("\033[92mlogin successful ! ")
                    if role == "admin":
                        ob = AdminMenu()
                        ob.show_menu()

                    elif role == "staff":
                        ob = StaffMenu()
                        ob.show_menu()
                    return
                    
            print("\033[93minvalid username and password!")
        except Exception as e:
            print(e)
