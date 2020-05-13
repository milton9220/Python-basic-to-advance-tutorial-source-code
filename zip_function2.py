l1=[1,3,5,7]
l2=[2,4,6,8]
#li=[(1,2),(3,4),(5,6)]
#ekhn ei list theke 3 ta touple k ek shate join otthat 1,3,5 and 2,4,6 korar jonno
#print(list(zip(*li)))

#ekhon 2 ta touple ke alada korar jonno ei method

#l1,l2=zip(*li)
#print(l1)
#print(l2)

#ekhon 2 ta list l1 and l2 ar moddhe maximum value show kora
new_list=[]
for pair in zip(l1,l2):
    max_value=max(pair)
    new_list.append(max_value)

print(new_list)
#upore first a loop a zip function l1 ar l2 ar moddhe combine kore pair a thake just like that [(1,2),(3,4),(5,6)]
#then pair er shate compare kore i mean first loop a 1,2 er shate then baki gular

