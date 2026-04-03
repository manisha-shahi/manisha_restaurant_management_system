
from app.division.json_manage import Json_Class
from app.division.validation import Validation
from app.logs.logger import write_log
from getpass import getpass

listdata = []
class Registration:
       
    def signup(self):
        try:
            json_obj1 = Json_Class()
            listdata = json_obj1.read_user()
            data = {}
        
            for i in range(3):
                data["username"] = input("\033[94m please enter username : ").strip().lower()
                obj1=Validation()
                Name = obj1.username_validation(data["username"])
                if Name:
                    break
                else:
                    print(f"\033[97m Attempts left: {2-i}")
            else:
                return

            for i in range(3): 
                data["password"] = getpass("\033[94m please enter password : ").strip()
                obj2 = Validation()
                Paasword = obj2.password_validation(data["password"])
                if Paasword:
                    break
                else:
                    print(f"\033[97m Attempts left: {2-i}")
            else:
                return

            for i in range(3):
                data["role"] = input("\033[94m please enter role admin/staff : ").strip().lower()
                obj3 = Validation()
                Role = obj3.role_validation(data["role"])
                if Role:
                    break
                else:
                    print(f"\033[97m Attempts left: {2-i}")
            else:
                return 

            for i in range(3):
                data["email_id"] = input("\033[94m please enter your email id :" ).strip().lower()
                obj4 = Validation()
                Emailid = obj4.email_validation(data["email_id"])
                if Emailid:
                    break
                else:
                    print(f"\033[97m Attempts left: {2-i}")
            else:
                return
            
            for i in range(3):
                data["mobile"] = input("\033[94m Enter mobile number: ").strip()
                obj5 = Validation()
                Mobile = obj5.mobile_no_validation(data["mobile"])
                if Mobile:
                    break
                else:
                    print(f"\033[91m Attempts left: {2-i}")
            else:
                return
            
            for i in range(3):
                data["aadhar"] = input("\033[94m Enter Aadhaar number: ").strip()
                obj6 = Validation()
                Aadhar = obj6.aadhar_validation(data["aadhar"])
                if Aadhar:
                    break
                else:
                    print(f"\033[91m Attempts left: {2-i}")
            else:
                return
            
            for i in range(3):
                data["city"] = input("\033[94m Enter city: ").strip().lower()
                obj = Validation()
                city = obj.city_validation(data["city"])
                if city:
                    break
                else:
                    print(f"Attempts left: {2-i}")
            else:
                return

            for i in range(3):
                data["qualification"] = input("Enter qualification: ").strip().lower()
                obj7 = Validation()
                Qualification = obj7.qualification_validation(data["qualification"])
                if Qualification:
                    break

            for i in range(3):
                data["language"] = input("\033[94m Enter languages you know ( hindi / english ): ").strip().lower()
                obj8 = Validation()
                Language = obj8.language_validation(data["language"])
                if Language:
                    break


            if Name and Paasword and Role and Emailid and Mobile and Aadhar and Qualification and Language :
                listdata.append(data)
                json_obj1.write_user(listdata)
                print("\033[95m signup successful")
                
                write_log("Signup successful: " , data["username"])
               
            else:
                print("\033[91m signup not successfully")
                write_log("signup not successfully :" , data["username"])
        
        except Exception as e:
            print("Error:",e)
            write_log("ERROR", "Error during signup: ",e)
        


    
        

