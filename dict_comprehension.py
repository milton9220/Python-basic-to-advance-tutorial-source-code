square={num:num**2 for num in range(1,11)}

for k,v in square.items():
    print(f"Square is {k}:{v}")

string="Milton"

count={char:string.count(char) for char in string}
print(count)

