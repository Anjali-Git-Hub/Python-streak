from csv import reader,DictReader
with open ("Read_csv.csv","r") as rf:
    # csv_reader=reader(rf)
    # for i in csv_reader:
    #     print(i)
    csv_reader=DictReader(rf)
    for i in csv_reader:
        print(i['name'])  
