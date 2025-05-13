# using encapsulation concept we can hide unnecessary data from user like the pin and balance. It can only be visible in the class and outside the class we cannot see this. also we can hide some methods if we want.
#  we use __ at the starting of the name of data or method to keep it private.

# Lets apply encapsulation on ATM class code:

# Nothing in python is truely private
class Atm:
    def __init__(self):
        # lets say we want to hide pin and balance data from users.
        # we added __ in start of pin like this __pin
        self.__pin = ""
        self.__balance = 0
        self.menu()
    #  we can use get and set methods to encapsulate
    def get_pin(self):
        return self.__pin
    
    def set_pin(self, new_pin):
        self.__pin = new_pin
        print("Pin changed")
    
    def menu(self):
        while True:
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
                self.check_balance()
            elif user_input == "5":
                print("Bye!")
                break
            else:
                print("Invalid input. Please try again.")
    
    def create_pin(self):
        self.__pin = input("Enter your new pin: ")
        print("Pin created successfully.")
    
    def deposit(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid pin.")
    
    def withdraw(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid pin.")
    
    def check_balance(self):
        temp = input("Enter your pin: ")
        if temp == self.__pin:
            print(f"Your balance is: {self.__balance}")
        else:
            print("Invalid pin.")
        

habiba = Atm()
habiba.get_pin()
habiba.set_pin()