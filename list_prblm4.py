
def even_odd(li):
    even=[]
    odd=[]
    lenth=len(li)
    
    for i in range(lenth):
        if li[i]%2==0:
            even.append(li[i])

        else:
            odd.append(li[i])
    
    output=[even,odd]   
    return output


n=int(input("How many list you want to add:"))
list=[]

for i in range(n):
    list_item=int(input("Enter your list:"))
    list.append(list_item)



print(even_odd(list))