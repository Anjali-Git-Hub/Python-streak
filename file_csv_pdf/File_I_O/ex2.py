with open("index.htm","r") as rf:
    with open ("ex2sol.py",'a') as wf:
        for i in rf:
            if "<a href=" in i:
                quote1=i.find("\"")
                quote2=i.find("\"",quote1+1)
                wf.write(f"{i[quote1+1:quote2]} \n")