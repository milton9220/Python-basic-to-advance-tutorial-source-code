from functools import wraps
def print_function(func):
    @wraps(func)
    def wrapper_func(*args,**kwarks):
        print(f"You are calling {func.__name__}")
        
        return func(*args,**kwarks)
    return wrapper_func    
      

   

 
@print_function
def addition(a,b):
    return a+b

print(addition(5,6))

