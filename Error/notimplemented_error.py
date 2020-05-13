#ami developer k emn error show korabe jeta take onno class a define korte hobe

class Animal:
    
    

    def sound(self):
        #print("meu meu") #but eikahne jodi sound meu meu dei tahole tahole jokon onno animal r jonno ei sound method use kora hobe tokon sobar khetre same sound sunabe .tai ei method ta k just error raise kore developer k bole dite hobe onno class a ei method k defined korte hobe. tai niche error raise kore dilam
        raise NotImplementedError("You have to defined every inherited classes")

class Dog(Animal):
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def sound(self):
        print("ghew ghew")

class Cat(Animal):
    def __init__(self,color,name):
        self.color=color
        self.name=name
    def sound(self):
        print("mew mew")


doggy=Dog("Pitu","black")
print(doggy.sound(),doggy.name,doggy.color)

