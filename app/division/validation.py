class Validation:
    def username_validation(self, username):

        if len(username) < 3:
            print("\033[91m username must be at least 3 characters")
            return False

        if len(username) > 15:
            print("\033[91m username must be less than 15 characters")
            return False

        if not username.isalpha():
            print("\033[91m username must contain only letters")
            return False

        else:
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
            return True


    def role_validation(self, role):

        if role == "":
            print("\033[91m role cannot be empty")
            return False

        if role not in ["admin", "staff"]:
            print("\033[91minvalid role")
            return False

        else:
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
        if email.count("@") != 1:
            print("\033[91m email must contain only one @")
            return False
        else:
            return True
            
    def mobile_no_validation(self,mobile_no):
        if not  mobile_no.isdigit():
            print("\033[91m please enter valid mobile number")
            return False
        
        if  len(mobile_no) != 10:
            print("\033[91m invalid mobile no")
            return False
        
        else:
            return True
        
    def aadhar_validation(self, aadhar):
        if not aadhar.isdigit():
            print("\033[91m Aadhaar must contain only digits")
            return False

        if len(aadhar) != 12:
            print("\033[91m Aadhaar must be 12 digits")
            return False

        else:
            return True
    def city_validation(self, city):

        if city == "":
            print("\033[91m city cannot be empty")
            return False

      
        if any(char.isdigit() for char in city):
            print("\033[91m city cannot contain numbers")
            return False

        if not city.replace(" ", "").isalpha():
            print("\033[91m city must contain only letters")
            return False

        
        if len(city) < 5:
            print("\033[91m city name too short")
            return False

        return True

    def qualification_validation(self, qualification):

        valid_qualifications = ["12th", "graduate", "bsc" , "bca", "mca", "btech", "mba"]

        if qualification not in valid_qualifications:
            print("\033[91m minimum qualification must be [12th,gradute, bsc,bca,mca,btech,mba] pass")
            return False
        else:
            return True
        
    def language_validation(self, language):

        valid_languages = ["hindi","english"]

        if language not in valid_languages:
            print("\033[91m invalid language")
            return False
        else:
            return True

   