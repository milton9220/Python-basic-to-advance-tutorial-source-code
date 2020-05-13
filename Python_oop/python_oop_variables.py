#There are two types of variables 
#1.instance variable
#2.class variable

class Car:
    whools=4 #class variable
    def __init__(self):
        self.mil=10    #This are instance variable
        self.com="BMW"

c1=Car()
c2=Car()
c2.mil=15
Car.whools= 4 #class variable a call and value assign kora
print(c1.mil,c1.com,Car.whools)
print(c2.mil,c2.com,Car.whools)        