user={
     'name' : "Miltu",
     'age'  :24
}

#print(user.get('name'))
#print(user.get('names'))
#if 'harsit' in user.values() eivabe o use korte pari

if user.get('name'):
    print(user['name'])
else:
    print("Not Present")   

#clear dictionary method

user.clear()
print(user)

#copy method in dictionary

user2=user.copy()
print(user2)