#if you want to sent list argument then you have to do this
#*num converts the list to unpack

def multi(*args):
    mul=1
    for i in args:
        mul*=i
    return mul

nums=[1,2,3,4]
print(multi(*nums))        