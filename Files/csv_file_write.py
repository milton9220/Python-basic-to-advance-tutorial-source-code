from csv import writer
from csv import reader
with open('Files/csv_file_2.csv','w',newline='') as wf: #newline eita diya hoi jate extra blank kono list make na hoi .jmn [] extra blank make hoi
    csv_write=writer(wf)
    csv_write.writerow(['name','country']) #write korar jonno method 2 ta 1.writerow 2.writerows
    csv_write.writerow(['Milton','Bangladesh'])
#ei write file k read korar jonno nicher ta.    
with open('Files/csv_file_2.csv','r') as r:
    csv_read=reader(r)
    next(csv_read)
    for row in csv_read:
        print(row)
