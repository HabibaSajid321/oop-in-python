# using inheritance the child can access -Data Members, -Methods, -Construtor
# But it cannot access the private data.
# Lets understand with the code 

class User:
    def login(self):
        print("login")

    def register(self):
        print("register")

class Student(User):
    def enroll(self):
        print("enroll")

    def review(self):
        print("review")

student1 = Student()
student1.enroll()
student1.login()

# but this is one way. the parent class cannot access the data of the child class.

# As we know child class can also inherit the constructor lets understand with the code.

class Car:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.__price = price

class newCar(Car):
    pass

s = newCar("Civic", "2020", "8000")
print(s.brand, s.model, s.__price)
s.__price()



#  Now lets verify is child class can access the private members.

        
