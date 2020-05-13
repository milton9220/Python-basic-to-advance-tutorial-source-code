#what is generator?
#generator hosce on fly a kisu value generate kore. jemon range(50) likhi 
for i in range(10):
    print(i)

#eikhane range ekta generator coz range function 1 theke 10 pojonto value every step a generate hoitese .but list generator na coz list memory age save hoi.but generator memory te save hoi na.jokon dorkar hoi then use hoi otthat number generate kora thake.
#kono number generate kore rakhle jokon amr dorkar hobe tokon use korlam

#generator ar example
def genrate(n):
    for i in range(n):
        yield i #yield er kaj number on the fly value generate kore

g=genrate(3)
#ekhon print korar jonno for loop use kore hobe coz generator object return kore.example
print(g)    #<generator object genrate at 0x01C1CCA0> eita print korse
#otthat eita k print korar jonno iterator korte hobe jeta foor loop kore
for result in g:
    print(result)
