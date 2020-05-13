class A:
    def __init__(self):
        print("In A Init")
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B(A):
    def __init__(self):
        super().__init__()
        print("In B Init")
    def feature3(self):
     print("This is feature 3")
    
    def feature4(self):
     print("This is feature 4")  

b=B() #ekhon question holo Class A te o constructor ace and class B te o constructor ace.jehutu Class B A ke inherit kortese taile B class ar object create korar somoy kon constructor call hobe?
#answer: Class B er constructor call hobe. ekn constructor A class er ta o ki call korar kono way ace?
# ace: just B class ar init method a super().__init__() use korlei hobe. upore seta use kora holo.    


#New Code with MRO means Method Resulation Order. ar eitar mane hossce suppose ami C ekta class korlam .ar Class a Class A,B k inherit otthat multiple inherit korlam .then jokon C class ar object create korbo tokon C class ar init() method a super().__init__() eita use korle Class A ar inti() method and j kono method run korbe .coz MRO first a nijer init method kaj kore then left a jai. niche ar code diya holo

class A:
    def __init__(self):
        print("In A Init")
    def feature1(self):
        print("This is feature 1")

    def feature2(self):
        print("This is feature 2")

class B:
    def __init__(self):
        super().__init__()
        print("In B Init")
    def feature3(self):
     print("This is feature 3")
    
    def feature4(self):
     print("This is feature 4")  

class C(A,B):
    def __init__(self):
        super().__init__()
        print("In C init")    

    def feature5(self):
     print("This is feature 5")
    
    def feature6(self):
     print("This is feature 6")     

c=C()
c.feature3()