def reverse(name):
    reverse=name[::-1]
    return reverse

value=input("Enter the name:")
output=reverse(value)
if output==value:
    print("Palindrome")
else:
    print("Not Palindrome")    

