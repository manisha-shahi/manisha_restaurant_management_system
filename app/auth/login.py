from app.file_handler.read_mode import Read_mode
from app.menu.all_menu import AdminMenu, StaffMenu
from getpass import getpass
from app.logs.logger import write_log

class Info: 
    def __init__(self):
        self.file = Read_mode()

    
    def Login(self):
        listdata = self.file.read_file("app/database/user.json")
        try:

            username = input("\033[93m please enter your name :").strip()
            password = getpass("\033[93m please enter your password:").strip()
            role = input("\033[93m please enter your role admin/staff :").strip().lower()

            for data in listdata:
                if( username == data["username"] and password == data["password"] and role == data["role"]):
                    print("\033[92m login successful ! ")
                    write_log("Login success: " + data["username"])
                    if role == "admin":
                        ob = AdminMenu()
                        ob.show_menu()

                    elif role == "staff":
                        ob = StaffMenu()
                        ob.show_menu()
                    return
                    
            print("\033[91m Invalid username and password!")
            write_log(f"Invalid username{username} and password{password}!")
        except Exception as e:
            print(e)
