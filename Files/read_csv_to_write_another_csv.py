from csv import DictReader,DictWriter
with open('Files/csv_file3.csv','r',newline='') as rf:
    dict_read=DictReader(rf)
    with open('Files/csv_file4.csv','w',newline='') as wf:
        dict_write=DictWriter(wf,fieldnames=['fname','lname','city'])
        dict_write.writeheader() #csv file a header lekha hoi
        for row in dict_read:
           fname,lname,city=row['first_name'],row['last_name'],row['city']
           dict_write.writerow({
               'fname':fname,
               'lname':lname,
               'city':city

           })
