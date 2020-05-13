def greatest(x,y,z):
    if x>y and x>z:
        print(f"{x} is greatest other than")
    elif y>x and y>z:
        print(f"{y} is greatest other than")
    else:
        print(f"{z} is greatest other than")


a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c=int(input("Enter the third value:"))

greatest(a,b,c)       