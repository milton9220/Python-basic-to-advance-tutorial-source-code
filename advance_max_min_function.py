names=["Monjur Hasan","Adnan "]

def fun(item):
    return len(item)
    
print(max(names,key=fun))  

student=[
    
        {'name':'Milton','age':24,'score':90},
        {'name':'Adu','age':25,'score':87}
    
]
def func2(item):
    return item.get('score')

print(max(student,key=func2))    

#another way
print(min(student,key=lambda item:item.get('score')))
