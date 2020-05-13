def even_odd(num):
    if num%2==0:
        return "Even"

    return "Odd"

value=int(input("Enter the value:"))

print(even_odd(value))