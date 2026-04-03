from app.division.json_manage import Json_Class
from app.menu.all_menu import AdminMenu, StaffMenu
from getpass import getpass
from app.division.validation import Validation
from app.logs.logger import write_log

class Info: 

    def Login(self):
        
        json_obj1 = Json_Class()
        listdata = json_obj1.read_user()
        
        try:
            for i in range(3):
                username = input("\033[93m please enter your name :").strip().lower()
                obj1=Validation()
                Name = obj1.username_validation("username")
                if Name:
                    break
                else:
                    print(f"\033[97m Attempts left: {2-i}")
            else:
                return
            
            for i in range(3):
                password = getpass("\033[93m please enter your password:").strip()
                obj2 = Validation()
                Paasword = obj2.password_validation(password)
                if Paasword:
                    break
                else:
                        print(f"\033[97m Attempts left: {2-i}")
            else:
                return
            for i in range(3):
                role = input("\033[94m please enter role admin/staff : ").strip().lower()
                obj3 = Validation()
                Role = obj3.role_validation(role)
                if Role:
                    break
                else:
                    print(f"\033[97m Attempts left: {2-i}")
            else:
                return 
            for data in listdata:
                if( username == data["username"] and password == data["password"] and role == data["role"]):
                    print("\033[92m login successful ! ")
                    write_log("Login success: " , data["username"])
                    if role == "admin":
                        ob = AdminMenu()
                        ob.show_menu()

                    elif role == "staff":
                        ob = StaffMenu()
                        ob.show_menu()
                    return
                    
            print("\033[91m Invalid username and password!")
            
        except Exception as e:
            print("Error:",e)
            write_log("ERROR", f"Error during signup: {e}")