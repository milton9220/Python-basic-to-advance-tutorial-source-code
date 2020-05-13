#In enumerate function show the index value with the item in listor topple
items=['alu','potol','shak']
for index,item in enumerate(items):
    print(f"{index}->{item}")

#you have to sent a one list and one string then if you find the that string in this list then return the list position .
#if you not find then return -1

def find_string(l,target):
    for index,item in enumerate(l):
        if item==target:
            return index

    return -1

list=["alu","potol","tomato","morich"]
print(find_string(list,"potol"))