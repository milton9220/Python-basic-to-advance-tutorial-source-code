# *args with normal parameter
#here normal parameter have to be written in the first
#here num value is 1 and args value is 2,3
def multi(num,*args):
    mul=1
    for i in args:
        mul*=i
    return mul

 
print(multi(1,2,3))       