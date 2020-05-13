
name,character=input("Enter two inputs:").split(",")
print(f"Length your name is:{len(name)}")
print(f"The total:{name.strip().lower().count(character.strip().lower())}")