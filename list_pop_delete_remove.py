n=int(input("How many data you want to add:"))
fruits=["mango","apple"]
count=len(fruits)

for i in range(n):
    input_value=input("Enter the value:")
    fruits.insert(count,input_value)

#pop=int(input("Which index value you want delete:"))

#fruits.pop(pop)
print(fruits)  

#delete=int(input("Which index value you want delete:"))

#del fruits[delete]

#print(fruits)

remove=input("which data you want to remove:")

fruits.remove(remove)
print(fruits)