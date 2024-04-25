# dictwriter class
from csv import DictWriter
with open("write2.csv",'w',newline="")as wf:
    # writerow,writerows
    csv_write=DictWriter(wf,fieldnames=["Name","Country","Age"])
    csv_write.writeheader()
    csv_write.writerows([
        {"Name":"anjali","Country":"India","Age":80},
        {"Name":"yashika","Country":"India","Age":40},
        {"Name":"song","Country":"Korea","Age":23}
        ])