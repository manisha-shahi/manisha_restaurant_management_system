from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from app.division.validation import Validation
from getpass import getpass

import json
import uuid

listdata = []
class Registration:
    def __init__(self):
        self.file = Read_mode()
        self.writefile = Write_mode()
        
    def signup(self):
        data = {}
        try:
            for i in range(3):
                data["username"] = input("\033[94please enter username : ").strip().lower()
                obj1=Validation()
                Name = obj1.username_validation(data["username"])
                if Name:
                    break
                else:
                    print(f"\033[97Attempts left: {2-i}")
            else:
                return

            for i in range(3): 
                data["password"] = getpass("\033[94please enter password : ").strip()
                obj2 = Validation()
                Paasword = obj2.password_validation(data["password"])
                if Paasword:
                    break
                else:
                    print(f"\033[97Attempts left: {2-i}")
            else:
                return

            for i in range(3):
                data["role"] = input("\033[94please enter role admin/staff : ").strip().lower()
                obj3 = Validation()
                Role = obj3.role_validation(data["role"])
                if Role:
                    break
                else:
                    print(f"\033[97Attempts left: {2-i}")
            else:
                return 

            for i in range(3):
                data["email_id"] = input("\033[94please enter your email id :" ).strip().lower()
                obj4 = Validation()
                Emailid = obj4.email_validation(data["email_id"])
                if Emailid:
                    break
                else:
                    print(f"\033[97Attempts left: {2-i}")
            else:
                return

            if Name and Paasword and Role and Emailid:
                listdata.append(data)
                print("\033[95msignup successful")
            else:
                print("signup not sccuessfuly")
        
        except Exception as e:
            print(e)
        


    
        

