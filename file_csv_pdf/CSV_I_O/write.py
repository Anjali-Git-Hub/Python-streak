# write --> writer , dictwriter
from csv import writer

with open("write.csv","w",newline="")as wf:
    csv_write=writer(wf)
    # methods --> writerow,writerows
    # csv_write.writerow(["name","country"])
    # csv_write.writerow(["anjali","india"])
    # csv_write.writerow(["song","korea"])

    csv_write.writerows([["name","country"],["anjali","india"],["song","korea"]])

