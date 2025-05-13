# In python we can pass our method written inside a class to a function as an argument. 
# lets learn through code 

class Customer:
    def __init__(self,name,gender):
        self.name = name
        self.gender = gender

def greet(customer):
    if customer.gender == "Male":
        print("Hello",customer.name,"Sir")
    else:
        print("Hello",customer.name, "ma'am")

# cust = Customer("Habiba","Female")
greet(Customer("habiba", "Female"))
