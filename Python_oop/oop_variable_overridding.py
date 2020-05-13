class A:
    class1="This is class1 class A variable"

    def __init__(self):
        self.var1="This is instance variable in class A"
        self.class1="This is instance variable class1 on class A"
        self.special="This is special"

class B(A):
    class1="This is class B in a Class A"

    def __init__(self):
         super().__init__()
         self.var1="This is instance variable in class B"
         self.class1="This is instance variable class1 on class B"
         
        
    

#class B class A k inherit korse.ar class er moddhe instance variable ace.jokon ami class B ar object create kore class1 variable k call korbo tokon jodi class B te instance variable na thake tahole class A ar instance variable show korbe jeta output 1.1 a dekha jasce. otthat class B ar class1 variable k class A ar instance variable override korse.ekhn jodi class B te class A er innit() method override kori otthat same kori tokon  tahole class B ar init method  show korbe.coz override kora hoise.output 1.2 te show kore.
b=B()
print(b.class1) #output 1.1:This is instance variable class1 on class A .before create instance variable in class B .
#output 1.2:This is after override innit() method class1 on class B 
print(b.special)#ekn super class use korar karone special value show korbe.
print(b.class1)#after adding super class ekn jodi super class ami B class ar instance variable ar age likhi tahole first superclass ar value asbe bt pore abr ei value class B ar value diye overrride hoe jabe. but pore super class use korle eitar ulta hobe.

#But ami chaitesi class A r method o show korbo plus Class B ar method o .tokon just super().__init__() use korle 2 tai show korbe jokon call kora hobe.niche example

#class B(A):
    #class1="This is class B in a Class A"

    #def __init__(self):
         #super().__init()__
         #self.var1="This is instance variable in class B"
         #self.class1="This is instance variable class1 on class B"
        