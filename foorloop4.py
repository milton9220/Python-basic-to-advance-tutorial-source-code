import random

wining_guess=random.randint(1,100)
print(wining_guess)
number=int(input("Guess the number:"))
print(number)
guess=0

for i in range(1,100):
    if wining_guess==number:
        print(f"you win!! you guessed {i} times")
        break
    elif wining_guess<number:
         print("To High")
         number=int(input("Guess again:"))
    elif wining_guess>number:
       print("TO Low")
       number=int(input("Guess again:"))
       
        
    