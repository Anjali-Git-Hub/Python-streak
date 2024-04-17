# list -- num - 1to 10
# l=[]
# for i in range (1,11):
#    l.append(i)
# print(l)

# l= [i for i in range(1,11)]
# print(l)


# square -- list 

# l=[i**2 for i in range (1,11)]
# print(l)



# def rev(l):
#     return [""+=i for i in range (l)]
# l=['abc','def','ghi']
# new=[]
# for i in l:
#     string=""
#     for j in range(len(i)-1,-1,-1):
#         string=string+i[j]
#     new.append(string)    
# print(new)

# new =[""+i[::-1] for i in l]
# print(new)


# print(rev(['abc','def','ghi']))



# list comprehension with if 
# even = [i*2 if i%2==0 else i for i in range (1,11) ]
# print(even)


# exercise - 

# inn=[True,False,1,["anjali","komal"],1.0,2,5]
# output =["1.0","2","5","1"]

# out=[str(i) for i in inn if type(i)==int or type(i)==float]
# print(out)



# matrix=[[1,2,3],[1,2,3],[1,2,3]]
# mat=[[i for i in range(1,4)] for i in range(3)]
# print(mat)