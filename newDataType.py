# We will create a new data type in python
#  for fraction functions

class Fraction:
    def __init__(self,n,d):    
        self.num = n
        self.den = d         
        #  n and d are neumerator and denumerator


    def __str__(self):
        return "{}/{}".format(self.num, self.den)
    
    def __add__(self,other):
        temp_num = self.num*other.den + other.num *self.den
        temp_den = self.den * other.den

        return "{}/{}".format(temp_num, temp_den)

x = Fraction(6, 9)
y = Fraction(8,12)
print(x, x+y)