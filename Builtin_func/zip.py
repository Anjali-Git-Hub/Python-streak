# zip function

# l1=["user1","user2","user3"]
# names=["anjali","rajni","komal"]
# lastName=["li","gariya","gariya"]


# unzip=[('user1', 'anjali'), ('user2', 'rajni'), ('user3', 'komal')]

# zipped=zip(*unzip)
# # for i in zipped:
# #     print(i)


# unzip 


# exercise


# l1=[2,4,3,5]
# l2=[0,8,1,2]
# maximum=[]

# for tuple in zip(l1,l2):
#     print(tuple)
#     maximum.append(max(tuple))

# print(maximum)


# def avg(*l):
#     new=[]
#     sum=0
#     for pair in zip(*l):
#         new.append(sum(pair)/len(l))
#     return new
         
        
# print(avg([1,2,3],[3,4,5],[2,6,7]))

avg=lambda *l:[sum(pair)/len(l) for pair in zip(*l)]
print(avg([1,2,3],[3,4,5],[2,6,7]))