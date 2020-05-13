#ekhon emn ta kaj korte hobe suppose onno ekta file a  ace
#Milton,6000 
#Adnan,10000
#Aminul,30000
#othat onno file ar ei line gula niye amr new file likhe hobe Milton salary is 6000

with open('Files/about.txt','r') as rf:
    with open('Files/set_about.txt','w') as wf:
        for lines in rf.readlines():
            name,salary=lines.split(',')
            wf.write(f"{name}'s salary is {salary}")
