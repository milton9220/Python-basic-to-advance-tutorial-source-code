n=int(input("How many data you want to add:"))
fruits=["mango","apple"]
count=len(fruits)
print(count)
for i in range(n):
    input_value=input("Enter the value:")
    fruits.insert(count,input_value)

print(fruits)
