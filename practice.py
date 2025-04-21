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

#  Example 

class New:

    def __init__(self):
        print("hello")
    def menu(self):
        pass

sbi = New()

# as I created this object sbi or class New() it prints hello automatically.

