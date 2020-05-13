from csv import reader
with open('Files/file.csv','r') as r:
    csv_reader=reader(r)
    next(csv_reader)
    for row in csv_reader:
        for single in row:
            print(single)
        
        
        
        
