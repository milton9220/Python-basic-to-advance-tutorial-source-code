#encapsulation bolte class ar baire theke data k protect kora and directly jate kew access korte na pare.
class Car:
    def __init__(self,speed,color):
        self.__speed=speed #__ means private
        self.__color=color
    
    def set_speed(self,value):
        self.__speed=value

    def get_speed(self):
        return self.__speed 
    def set_color(self,value):
        self.__color=value
    def get_color(self):
        return self.__color          
    
ford=Car(120,"red") 
maruti=Car(100,"black")
ford.set_speed(300)
ford.__speed=400 #eikhane private data access kore change korte chaisilam bt no change ager value e show kore.
print(ford.get_speed()) 
#print(ford.__color) #color private data access korar jonno method use kore then access korte hobe.
print(ford.get_color())
#private data directe acces kora jai na. access korar jonno kono method use kore take call kore use korte hoi.jmn upore car ar speed direct access kora jai na tai get set method use kore acces korte hoise. 