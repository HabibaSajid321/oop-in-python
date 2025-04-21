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
            print("Create Pin")
        elif user_input == "2":
            print("deposit")
        elif user_input == "3":
            print('Withdraw')
        elif user_input == "4":
            print("balance")
        else:
            print("bye")