class Validation:
    def username_validation(self, username):

        if len(username) < 3:
            print("\033[91m1musername must be at least 3 characters")
            return False

        elif len(username) > 15:
            print("\033[91username must be less than 15 characters")
            return False

        elif not username.isalpha():
            print("\033[91username must contain only letters")
            return False

        else:
            print("\033[92valid username")
            return True   
    

    def password_validation(self, password):

        if password == "":
            print("\033[91password cannot be empty")
            return False

        elif len(password) < 6 or len(password) > 20:
            print("\033[91password must be between 6 and 20 characters")
            return False

        elif " " in password:
            print("\033[91password cannot contain spaces")
            return False

        else:
            print("\033[92valid password")
            return True


    def role_validation(self, role):

        if role == "":
            print("\033[91role cannot be empty")
            return False
            role = role.strip().lower()

        if role not in ["admin", "staff"]:
            print("\033[91invalid role")
            return False

        else:
            print("\033[92valid role")
            return True

    def email_validation(self, email):

        if email == "":
            print("\033[91email cannot be empty")
            return False

        elif " " in email:
            print("\033[91email cannot contain spaces")
            return False

        elif "@" not in email or ".com" not in email:
            print("\033[91invalid email")
            return False

        else:
            print("\033[92valid email")
            return True