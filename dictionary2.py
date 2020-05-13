user={
    'name':'milton',
    'age' :24,
    'movies':['3 idiotes','charli'] 
}

#if 'milton' in user.values():
    #print("Present")

#else:
    #print("Not Present")

for i in user.values():
     print(i)   

for key,value in user.items():
    print(f"Key is {key} and value is {value}")