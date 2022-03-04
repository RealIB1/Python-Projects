import time

print("*" * 21)
print("Welcome to ABSA BANK\n24/7 ATM Service.")
print(time.strftime('%B %d, %Y %H:%M:%S\n%Z'))
print("*" * 21)
print("Please insert Your Card!")
time.sleep(2)
print("Please wait!")
time.sleep(3)


def main():
    f_name = "Ibrahim"
    balance = float(2000.97)
    chances = 3
    while chances >= 0:
        go_back = "Y"
        pin = int(input("Enter You PIN: "))
        time.sleep(1)
        if pin == 4233:
            print("You Entered Your PIN Correctly.")
            print("Select from the options below\n")
            print("Press 1 to Withdraw.")
            print("Press 2 to Deposit.")
            print("Press 3 to Check Balance.")
            print("Press 4 to Return Card.")
            options = int(input("Press between 1 and 4: "))
            if options == 1:
                print("How Much Would You Like to Withdraw? 10,20,50,100,200, Press 1 for other options")
                withdraw = float(input("Enter the amount to withdraw: "))
                if withdraw in [10, 20, 50, 100, 200]:
                    balance -= withdraw
                    print("Please wait while the ATM Dispense Cash!")
                    time.sleep(2)
                    print(f"You have successfully withdraw ${withdraw}0")
                    print(f"\nYour New Balance ${balance}")
                    go_back = input("Would you like to go back? (Yes/No): ")
                    if go_back in ("N", "n", "no", "No",):
                        print(f"\n{f_name} Thank for Banking With Us!")
                        break
                elif withdraw is not [10, 20, 50, 100, 200]:
                    print("Invalid amount, Please enter 10,20,50,100,200.\n")
                    print("How Much Would You Like to Withdraw? 10,20,50,100,200 or Press 1 for other options")
                    withdraw = float(input("Enter the amount to withdraw: "))
                    balance -= withdraw
                    print("Please wait while the ATM Dispense Cash!")
                    time.sleep(2)
                    print(f"You have successfully withdraw ${withdraw}0")
                    print(f"\nYour New Balance ${balance}")
                    go_back = input("Would you like to go back? (Yes/No): ")
                    if go_back in ("N", "n", "no", "No",):
                        print(f"\n{f_name} Thank for Banking With Us!")
                        break
            elif options == 2:
                deposit = float(input("Please enter deposit amount: "))
                balance += deposit
                print(f"\nYou have successfully deposited ${deposit}0 into your account.")
                print(f"Your New Balance ${balance}")
                print(f"Current Balance ${balance}")
                go_back = input("Would you like to go back? (Yes/No): ")
                if go_back in ("N", "n", "no", "No",):
                    print(f"\n{f_name} Thank for Banking With Us!")
                    break
            elif options == 3:
                print(f"Current Balance is ${balance}\nMain Balance is ${balance}")
                go_back = input("Would you like to go back? (Yes/No): ")
                if go_back in ("N", "n", "no", "No",):
                    print(f"\n{f_name} Thank for Banking With Us!")
                    break
            elif options == 4:
                print("Please wait while you card is returned.")
                time.sleep(2)
                print(f"\n{f_name} Thank for Banking With Us!")
                break
            else:
                print("Please select the right option between 1 and 4")
        elif pin != 4233:
            print("Incorrect PIN\nPlease Enter Correct PIN")
            chances -= 1
            if chances == 0:
                print("Your Card has been Blocked!\nPlease Visit any of our Branches for Help!")


if __name__ == "__main__":
    main()
