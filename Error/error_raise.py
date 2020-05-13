#kono error asle setar reply:
def add(a,b):
    if(type(a)is int) and (type(b)is int):
        return a+b
    else:
        raise TypeError("Ops you have enterted wrong data type")

print(add("3","3"))