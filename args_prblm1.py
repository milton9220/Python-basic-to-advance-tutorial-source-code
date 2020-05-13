def tringle(num,*args):
    result=1
    final_result=[]
    for i in args:
        result=i**num
        final_result.append(result)
    return final_result

value=[1,2,3]
print(tringle(3,*value))   

#list comprehension code
def to_tringle(num,*args):
    
        return[i**num for i in args]


print(to_tringle(3,1,2,3))
