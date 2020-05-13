#there are 3 types of method
#1.Instance method.
#2.class method
#3.static method

class Student:
    school="A.K High School"
    def __init__(self,m1,m2,m3):
        self.mark1=m1
        self.mark2=m2
        self.mark3=m3

    @classmethod #classmethod r jonno ei decorator likhte hobe 
    def get_school_name(cls):#kono class variable niye kaj korte hole ei class method use korte hobe.ar ei method hosce class method
        print(cls.school)


    def avarage_mark(self): #this is instance method .coz ei method a self passing kortesi.ar self passing mane object pass kortesi. ar ei self object k belongs kore .jar karone ei method instance method. ar eita k instance method arekta karon hoscce ami jodi kono object r average jante chai tokon bolte hobe s1 na s2 er object tai self a object pass kora hoi.
        return(self.mark1+self.mark2+self.mark3)/3    
    
    @staticmethod
    def info(): #This is a static method
        print("This is static method ")
s1=Student(70,80,90)
s2=Student(80,60,75)

print(s1.avarage_mark())
print(s2.avarage_mark())
Student.get_school_name()
Student.info()
#kokon amra static method use korbo.jokon emn ekta method dorkar porbe jeita te instance variable and class variable ar dorkar porbe na tokon static method make korbo
