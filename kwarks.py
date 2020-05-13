#if you sent keyword argument to the function then we use to this method
#** this the method to set a parameter to the function 
#**kwarks receive a parameter as a dictionary

def kwarks(**kwarks):
    for k,v in kwarks.items():
        print(f"{k}={v}")

kwarks(firstname="Monjur Hasan",lastname="Milton")

#dictionary unpacking
#if you sent to a function as a dictionary then we have to unpack the dictionary
def kwarks_pack(**kwarks):
    for k,v in kwarks.items():
        print(f"{k}={v}")

dic={'name':'milton','age':24}
kwarks_pack(**dic)       