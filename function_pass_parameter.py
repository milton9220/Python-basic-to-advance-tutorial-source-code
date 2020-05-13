def sum(a):
    
    
    return a**2

def my_map(function,list):
    new_list=[]
    for i in list:
        new_list.append(sum(i))

    return new_list

print(my_map(sum,[1,2,3]))           