print("Welcome to Our Service, Please Sign Up below.")

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")

print("\n Hint: Select simple and memorable username for easy reminder.")
username = input("Enter username: ")
print("\nHint: Your password must be at least 8 characters.\n Password must "
      "contain A-Z, a-z, 0-9 and special characters.")
password = None
while len(str(password)) < 8:
    print("Password must be least 8 characters and must contain special characters.")
    password = input("Enter your password: ")
    if len(password) >= 8:
        print(f"{f_name.capitalize()}, You've successfully Signed up for our Service.\n Your username is {username}")


def user():
    print("\nWelcome to Tech Hashes... \n Enter Username and Password to Login.")
    # username1 = input("Username: ")
    # password1 = input("Password: ")

    while True:
        username1 = input("Username: ")
        password1 = input("Password: ")
        if username1 == username and password1 == password:
            print(f"\nYou are successfully logged in.\n Welcome {f_name.capitalize()}.")
            return True
        else:
            print("Invalid username or password, Please try again!")


user()
