class Validation:
    def username_validation(self, username):

        if len(username) < 3:
            print("\033[91m username must be at least 3 characters")
            return False

        if len(username) > 15:
            print("\033[91m username must be less than 15 characters")
            return False

        if not username.isalpha():
            print("\033[9m username must contain only letters")
            return False

        else:
            print("\033[92m valid username")
            return True   
    

    def password_validation(self, password):

        if password == "":
            print("\033[91m password cannot be empty")
            return False

        if len(password) < 6 or len(password) > 20:
            print("\033[91m password must be between 6 and 20 characters")
            return False

        if " " in password:
            print("\033[91mpassword cannot contain spaces")
            return False

        else:
            print("\033[92m valid password")
            return True


    def role_validation(self, role):

        if role == "":
            print("\033[91m role cannot be empty")
            return False

        if role not in ["admin", "staff"]:
            print("\033[91minvalid role")
            return False

        else:
            print("\033[92m valid role")
            return True

    def email_validation(self, email):

        if email == "":
            print("\033[91m email cannot be empty")
            return False

        if " " in email:
            print("\033[91m email cannot contain spaces")
            return False

        if "@" not in email or ".com" not in email:
            print("\033[91m invalid email")
            return False

        else:
            print("\033[92m valid email")
            return True
        
    def table_no_validation(self,table_no):
        if not table_no.isdigit():
            print("only number are valid")
            return False
        
        if table_no <= 1 or table_no >= 55:
            print("please enter valid number ")
            return False
        
        else:
            print("valid table no")
            return True
            
    def people_validation(self,people):
        if not people.isdigit():
            print("please enter valid number")
            return False
        else:
            print("valid people ")
            
    def mobile_no_validation(self,mobile_no):
        if mobile_no.isdigit():
            print("please enter valid mobile number")
            return False
        
        if len(mobile_no) == 10:
            print("\033[91m invalid mobile no")
            return False
        
        else:
            print("valid mobile number")
        

    

   