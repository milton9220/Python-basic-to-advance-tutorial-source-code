#dicreader diye csv file dictionary akare extract kora jai.otthat key soho extract kora jai.jmn ager csv file kaj kore dekhi
from csv import DictReader
with open('Files/file.csv','r') as r:
    dic_reader=DictReader(r)
    for row in dic_reader:
        print(row['name'])
        print(row['phone'])  #ekhon amr eccha moto ja print korte mon chai tai print korte parbo
