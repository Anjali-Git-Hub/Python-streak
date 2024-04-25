# without enumerate function 

# track the position of items of the lists or tuple

# pos=0
list=["anjali","rajni"]
d1={
    "name":"anjali",
    "age":6
}
# for i in list:
#     print(f"{pos} : {i} ")
#     pos+=1

for pos,name in enumerate(d1):
    print(pos,name)


# exercise 

# l=["anjali","rajni"]
# find="komal"
# flag=0
# for pos,name in enumerate(l):

#     if find==name:
#         flag=1
#         print(pos)
# if flag==0:
#     print(-1)
    

