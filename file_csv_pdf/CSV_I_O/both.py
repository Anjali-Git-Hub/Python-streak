from csv import DictReader,DictWriter

with open ("Read_csv.csv" , 'r') as rf:
    with open ("both.csv" , 'w',newline="") as wf:
        read_csv=DictReader(rf)
        write_csv=DictWriter(wf,fieldnames=["Name","Age","Occupation"])
        write_csv.writeheader()
        for i in read_csv:
            write_csv.writerow({
                "Name":i['name'],
                "Age":i['age'],
                "Occupation":i['occupation']
            })
            