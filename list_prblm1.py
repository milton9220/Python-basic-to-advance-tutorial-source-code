
def square_list(list):
    square_value=[]
    for i in list:
        square_value.append(i**2)

    print(square_value )    

n=int(input("how many values you want to add list:"))
list_item=[]
count=len(list_item)

for i in range(n):
    item=int(input("Enter value:"))
    list_item.insert(count,item)
    list_item.sort()
    print(list_item)

square_list(list_item)
