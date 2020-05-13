#jokon amra kono class ar object create hoi computer ar heap memory te.ar seikhane ei object ar ekta address thake.ar ei address print korar jonno id() ei method use korte hoi.example

#class Computer:
    

#c1=Computer()
#print(id(c1)) # 16081272 ei value hosce c1 object ar address.

#every object ar jonno different different address thake.
#jokon e ami j kono ekta object create korte jabo tokon e space create hobe.
#size of this memory depends on the number of variables
#who allocate size this  memory?
#constructor ei memory size gula allocate kore.otthat koto size er object hobe eita constructor kore

#c1=Computer() eikhane Computer() hossce constructor. jokon object create korar somoy constructor lekha hoi tokon e __init__ method call hoi

class Person:

    def __init__(self):
        self.name="Milton"
        self.age=24

    def update(self):
        self.age=30 

    def compare(self,other_object):
        if self.age==other_object.age: #eikhane self.age a p1 object r value ar other_object.age a p2 ar value
            return True

        else:
            return False           

p1=Person()
p2=Person()
#ekon to 2 ta object er same value asbe .tai amra different value assign korte pari

#bt ekhon chaitesi ami p1 or p2 ar value update korar jonno tokon ki korbo?
#p1.update() #but their are 2 objects.so update method kivabe bujbe kon object ar jonno ami value change korbo? ar eita bujar jonnoi self keyword likhte hoi.self er moddhe jei object er kaj korte chaibo j kono method a sei method a oi object as a argument pass hoi .sei object er jonno method kaj kore

#self is a pointer which point the object

# 2 object ar value er moddhe compare korar jonno

if p1.compare(p2): #eikhane compare ekta method jeikhane 2 ta object er value compare kore.ar compare method er self a jabe p1 object ,ar onno argument a jabe p2 object.
    print("They are same")

else:
    print("They are different")