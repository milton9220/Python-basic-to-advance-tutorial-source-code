# here * receives input as a tuple

def total (*args):
    total=0
    for num in args:
        total+=num
    return total

print(total(1,2,3,4))