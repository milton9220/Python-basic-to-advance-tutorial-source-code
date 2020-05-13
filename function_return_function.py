def outter_func():
    def inner_func():
        print("This is inner function")
    
    return inner_func

var=outter_func()
var()  

def outer(msg):
    def inner():
        print(f"This is inner and outer message {msg}")

    return inner

f=outer("Hellow")
f()