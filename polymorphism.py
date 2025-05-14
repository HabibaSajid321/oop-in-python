# Polymorphism has Method Overriding, Method Overloading, Operator Overloading.


class Phone:
    def __init__(self, price, brand):

        self.price = price
        self.brand = brand


    def buy(self):
        print("buying new phone")
    
class NewPhone(Phone):

    def buy(self):
        print("Hi new phone")
# Method Overriding as in the parent class we have the same function named buy. 

s = NewPhone("1990", "Apple")
print(s.brand, s.price)
# If I run s.buy() it will return the value of its own class not the value of parent class. This is the concept of overriding
s.buy()

