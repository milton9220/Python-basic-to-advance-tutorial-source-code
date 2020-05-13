def reverse_list(li):
    reverse=[]
    lenth=len(li)
    for i in range(lenth):
        pop_value=li.pop()
        reverse.append(pop_value)

    return reverse    

list=[]
n=int(input("how many list item want to add:"))

for i in range(n):
    list_item=int(input("Enter the list item:"))
    list.append(list_item)

print(reverse_list(list))