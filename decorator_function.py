#decoration function r kaj hosce j kono function ar extra kisu kaj kore without oi function extra kisu na kore.

def decorator_func(any_func):
    def wrapper_fun():
        print("This is awesome function")
        any_func()

    return wrapper_fun    

#def func1():
    #print("This is function 1")

def func2():
    print("This is function 2")

#ekhon uporer 2 ta function a extra This is awesome function ei lekha ta show korate chaitesi without func1 and func2 te print na kore then decoration function lagbe .jeta upore kora ace

#var=decorator_func(func1)
#var()
var2=decorator_func(func2)
var2()
#first a decoration function fun1 function ta pass kori then decoration ar inner function otthat wraper function ta run kore .ar oi function a first a print kore lekha ta then any function call hobe .otthat any function bolte func1 ta call hobe.wrapper er moddhe func1 call hobe.sudu func1 e an j fucntion pass kora hobe seita call hobe.

#ekhon decorator function r moddhe func1 or func2 function argument na pathaio ei function k call kora jai.

#shorcut
@decorator_func #just decorator function r name likhle then just func1 call korlei decorator function run hobe.ei khetre decorator function call korte hobe na
def func1():
    print("This is function 1")

func1()