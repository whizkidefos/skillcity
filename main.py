# Cash machine program
# def withdraw():
#     balance = 1000
#     pin = int(input("Enter your pin: "))
#     amount = int(input("Enter the amount you want to withdraw: "))
#     if amount <= balance and pin == 1234:
#         print("Cash is being dispensed...")
#         print("You have withdrawn", amount, "and your new balance is", balance - amount)
#     elif pin != 1234:
#         print("Invalid pin")
#     elif amount > balance:
#         print("Insufficient funds")
#     else:
#         print("You've either entered an invalid pin or an invalid amount. Please try again.")
    
# withdraw()


# ATM machine program
def atm_machine():
    balance = 1000
    pin = int(input("Enter your pin: "))
    print("ATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    choice = int(input("Choose an option: "))
    if choice == 1 and pin == 1234:
        print("Your current balance is: £", balance)
    elif choice == 2 and pin == 1234:
        deposit = int(input("Enter the amount you want to deposit: "))
        balance += deposit
        print("Successfully deposited £", deposit)
        print("Your new balance is: £", balance)
    elif choice == 3 and pin == 1234:
        withdraw = int(input("Enter the amount you want to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Cash is being dispensed...")
            print("You have withdrawn £", withdraw)
            print("Your new balance is: £", balance)
        else:
            print("Insufficient funds")
    elif choice == 4 and pin == 1234:
        print("Thank you for using the ATM. Goodbye!")
    else:
        print("Invalid pin or choice. Please try again.")



atm_machine()