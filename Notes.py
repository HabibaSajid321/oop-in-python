a = 7
print(type(a))
# in python everything is an object
# This will result <class 'int'>
# here a is the object of class 'int'

L = [1,2,3,4]
L.append(5)
print(L)

L = 7
# L.app

# Obbject Literal 

# this is the original syntax of the object 
# for example class is Car and WangonR is the object The syntax is: 
# WangonR = Car()

# But as we know list is also an object but we create the list like :
# This is the object litterals way:
List = [1,2,4] 
# : here myList is an object of list class but the syntax is different
# Reason is we have object literals for Built in data types to create objects in the easiest way
# We can Also create list like this 
# 
# This is the original way 
myList = list()
myList.append(1)
print(myList)

# creating string 
City = str()
print(type(City))


# Method vs Function
# -- Method is a special function written inside a class
# -- Function is a normal function 
# Len is a function len(L) 
#  We call the function and method in different ways:
# ----- Calling method 
#  L.append(1) : this is a method
#  Method can only be accessed by the object of that class.


# IN class whenever we declared variables we have to create them inside __init__ Method 



                   #  __init__ :

        #   ---init is the constructor
        #  constructor is a special method jiske andr rkha huwa code automatically execute hota hai jesay hi hum us class ka object bnatay hain.
        # some methods in python are called special/Magic/Dunder methods
        # Constructor is one of the magic methods in python. There are alot more magic methods in python. their syntax is like __method__.
        # all thes are pre-defined
#  Example 

class New:

    def __init__(self):
        print("hello")
    def menu(self):
        pass

sbi = New()

# as I created this object sbi or class New() it prints hello automatically.

# we use contructor if we do not want to share the control of something with user.
# We do configuration like tasks in constructor.



        #    SELF keyword
# Self is the object 
# class mai har object hi self hai. For every object there is a uniqie id of self same as the name of object.
# Jis object k sth abhi kam kr rhay ho wahi self hai 

# Why do we need self:
#  Concept 1:
# OOP ka fundamental concep is class mai data or methods hotay hain or in dono ko access srf class ka object kr skta hai.
# Concept 2:
# Class mai khud ek method apne class k dosre method ya data ko access nhi kr skta 
# But jaha pe hmai ek mothod ko dosre method ko access krna hoga or wo object yaha self k through aayga.


                            # Instance Variable 
# The variables we create inside a class are called instance variables. and for each object their value is changing

#                             Reference variable
# object create krtay time hum object ko jis variable mai store krtay hain is called reference variable
# Example : habiba = Atm() 
# habiba is the reference variable here.
