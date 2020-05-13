import random
random=random.randrange(1, 100, 3) 

user_input=int(input("Enter the lucky number:"))
if random==user_input:
    print("You Win!!!")

elif random<user_input:
    print("Too High")
elif random>user_input:
    print("To Low")