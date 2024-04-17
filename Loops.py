# while loop 
# num=input("enter a number ")
# i=0
# sum=0
# while(i<len(num)):
#     sum+=int(num[i])
#     i+=1
# print(sum)


# for loop 
# sum=0
# for i in num:
#     sum+=int(i)
# print(sum)


# ask a user his/her name and count the letters and print


# name=input("enter your name")
# i=0
# while (i<len(name)):
#     print(f"{name[i]}  :  {name.lower().count(name[i].lower())}")
#     i+=1


# for i in range(len(name)):
#     print(f"{name[i]}  :  {name.lower().count(name[i].lower())}")



# backward counting using range function 


# for i in range (10,-1,-1):
#     print(i)



name =input("enter your name ");
dummy=""
for i in range (len(name)):
    if name[i].lower() not in dummy.lower():
        dummy+=name[i]
        print(f"{name[i]}   :  {name.lower().count(name[i].lower())} ")









