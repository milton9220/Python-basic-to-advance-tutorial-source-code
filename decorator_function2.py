#decorator 1 function to amra kaj korsilam without kono argumant pass na kore.but emn jodi hoi amdr emn ekta function ace jar argument ace then ager tai kaj hobe na .se khetre new vabe korte hobe

def decorator_fun(any_function):
    def wrapper_fun(*args,**kwarks):
        print("This is awesome function")
        any_function(*args,**kwarks) #args and kwarks mean ami jei function k call korbo oi function paramater jotogula thakuk ba na thakuk doesnt matter

    return wrapper_fun
@decorator_fun
def func1(a):
    print(f"This is function with argument {a}")    

func1(2)

@decorator_fun
def func2():
    print("This is func2 function")

func2()      
#eikhane *args use kora hoise jate kono function ar parametter thakle ba  na thakleo jate oi function ta chole and j koita argumant ala function jate kaj kore and program a error na dekhai. ar **kwarks use kora hoise dictionary o jate argument pass kora jai
#fun=decorator_fun(func1(12)) 
#fun()