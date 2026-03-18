class Validation:
    def username_validation(self, username):

        if len(username) < 3:
            print("username must be at least 3 characters")
            return False

        elif len(username) > 15:
            print("username must be less than 15 characters")
            return False

        elif not username.isalpha():
            print("username must contain only letters")
            return False

        else:
            print("valid username")
            return True   
    

    def password_validation(self, password):

        if password == "":
            print("password cannot be empty")
            return False

        elif len(password) < 6 or len(password) > 20:
            print("password must be between 6 and 20 characters")
            return False

        elif " " in password:
            print("password cannot contain spaces")
            return False

        else:
            print("valid password")
            return True


    def role_validation(self, role):

        if role == "":
            print("role cannot be empty")
            return False
            role = role.strip().lower()

        if role not in ["admin", "staff"]:
            print("invalid role")
            return False

        else:
            print("valid role")
            return True

    def email_validation(self, email):

        if email == "":
            print("email cannot be empty")
            return False

        elif " " in email:
            print("email cannot contain spaces")
            return False

        elif "@" not in email or ".com" not in email:
            print("invalid email")
            return False

        else:
            print("valid email")
            return True