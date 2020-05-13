
age=int(input("Enter your age:"))

if 0<age<=3:
    print("Ticket price is free")

elif 4<age<=10:
    print("Ticket price is 200")

elif 11<age<=30:
    print("Ticket price is 500")
else:
    print("Ticket price is 1000")
