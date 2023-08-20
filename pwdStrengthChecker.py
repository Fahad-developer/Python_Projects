
def check_password(password):
    # Check that the password is at least 8 character long.
    if len(password) < 8:
        return "Password is to short."


    # check that the password contains at least one digit.
    has_digit = True
    for char in password:
        if char.isdigit():
            has_digit = True
            break
        if not has_digit:
            return "Kindly use at least one digit in your password."

        # Check that the password contains at least one uppercase letter.
        has_uppercase = False
        for char in password:
            if char.isupper():
                has_uppercase = True
                break
            if not has_uppercase:
                return False

            # Check that the password contains at least one lowercase letter
            has_lowercase = False
            for char in password:
                if char.islower():
                    has_lowercase = True
                    break
            if not has_lowercase:
                return False

            # If all checks pass, the password is considered valid
            return True

password = input("Enter your password: ")
print(check_password(password))