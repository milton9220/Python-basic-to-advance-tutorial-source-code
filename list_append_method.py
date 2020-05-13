fruits=[]
n=int(input("How many fruits you want to add:"))

for i in range(n):
    input_value=input("Enter the value:")
    fruits.append(input_value)

for i in range(n):
    print(fruits[i])   