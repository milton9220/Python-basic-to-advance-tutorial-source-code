class Student:

    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
        self.lap=self.laptop() #inner class eikhane call hoise
    def show(self):
        print(self.name,self.roll)
        self.lap.show()

    class laptop:
        def __init__(self):
            self.cpu="ci5"
            self.ram="4gb"

        def show(self):
            print(self.cpu,self.ram)            

s1=Student("MIlton",1)
s2=Student("Abrar",2)
s1.show()
s2.show()
#ekhon inner class call korar 2 ta option ace .first inner class ar baire outer class ar vitore a innit method a jate object create howar somoy e call hoi.