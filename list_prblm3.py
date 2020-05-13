def reverse_character(li):
    reverse=[]
    
    for i in li:
        
        reverse.append(i[::-1])

    return reverse    

list=[]
n=int(input("how many list item want to add:"))

for i in range(n):
    list_item=input("Enter the list item:")
    list.append(list_item)

print(reverse_character(list))