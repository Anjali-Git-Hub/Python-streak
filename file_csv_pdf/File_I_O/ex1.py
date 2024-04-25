rf= open("ex1.txt","r")
wf=open("exsol.txt","a")
for read in rf:
    name,point=read.split(",")
    wf.write(f"{name} having {point}")