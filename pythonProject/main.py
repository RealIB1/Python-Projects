"""
Hello, this is from Ibrahim, a beginner programmer.
"""


def names():
    name = input("Enter your name here: ")
    age = int(input("Enter your age: "))
    phone = int(input("Enter your phone number: "))
    if (name, age and phone) is not None:
        print(f"Thank you {name}, you've successfully register for our service..")
    else:
        print("Please provide your details!!")


names()


