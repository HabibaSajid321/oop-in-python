class Atm:
#    To define variables inside a class, we use the __init__ method.
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()
    
    def menu(self):
        user_input = input("""
                      Hello, How would you like to proceed?
                           1. Enter 1 to create pin
                           2. Enter 2 to deposit.
                           3. Enter 3 to Withdraw
                           4. Enter 4 to check balance
                           5. Enter 5 to exit
""")

        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            print("balance")
        else:
            print("bye")
    

    def create_pin(self):
        self.pin = input("Enter your pin")
        print("Pin created successfully")
    

    def deposit(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            self.balance = self.balance + amount
            print("Deposit Successfu;")
        else:
            print("Invalid Pin")
    
    def withdraw(self):
        temp = input("Enter your pin")
        if temp == self.pin:
            amount = int(input("Enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("Operation Successful")
            else:
                print("Insufficient Balance")
        else:
            print("Invalid pin")
    

    def check_balance(self):
        temp = input("Enter your pin")
        if temp == self.pin():
            print(self.balance)
        else:
            print("invalid pin")

    
