#pass mane kono method use na korle pass likhe dilei hobe.But must be use any method .otthat kono method declare kore khali rakha jabe na.
class Computer:
    
    def __init__(self,x,y):  #__int__ method just like a constructor.otthat object create kore somoy auto call hoi
        self.cpu=x  #eikhane x ar value assign korte hobe object a. ar self a object parameter pass hoi.jei object pass hoi oi object a x ar value assign korte hobe.tai eikhane self use kora.ar self ar por cpu lekha eita hosce variable.otthat cpu ar object er cpu variable a x assign kora
        self.ram=y
     

    def config(self): #eita ekta method just like function.       #every   Method should have "self" as first argument
    #self a object as a argument pass hoi .j object create kora hoi oi argument e pass hoi   
        print("Computer is",self.cpu,self.ram)#eikhane just cpu ar ram variable dile error dekhabe .coz cpu and ram is a local variable .ar tai  eita j object belongs otthat ei class ar object er object create korar somoy jei object ei config j object pass hoi  seta age likhte hobe.

com1=Computer("corei7","2gb")
com1.config()  
com2=Computer("corei8","8gb")
com2.config()      