def divide(a,b):
    try:

       return a/b

    except ZeroDivisionError:
        print("number is not divied..")   
    
    except TypeError:
        print("number must be integer...")

#x=int(input("Enter your first number:"))
#y=int(input("Enter your second number:"))
print(divide(10,'2'))
    
    
    
    