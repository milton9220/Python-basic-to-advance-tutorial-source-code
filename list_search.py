
fruits=[]

n=int(input("How many fruits you want to add:"))

for i in range(n):
    input_value=input("Enter the value:")
    fruits.append(input_value)

search=input("Which fruits you want to search:")

if search in fruits:
    print(f"{search} is here")
else:
    print(f"{search} is not here")
