mixed =["apple","mango",1,2,3,4]
# mixed[2:]=["papaya","litchi"]
# print(mixed)

# add elements in list 
# mixed.extend(["papya","juice"])
# print(mixed)

# insert - in a particular position 
# mixed.insert(1,["banana","limca"])
# print(mixed)

# join lists 
# fruits =["apple","mango"]
# vege=["brinjal","potato"]
# others=["1",2,3]
# mixed=fruits+vege+others
# print(mixed)


# delete data from list

# 1. pop method
fruits =["apple","mango"]
# fruits.pop(0)
# print(fruits)

# 2. del operator 
# del fruits[1]

# 3. remove method
# fruits.remove("mango")

# print(fruits)


# in keyword with list 
# if "mango" in fruits:
#     print("yes")



# compare the lists 
# list1=["mango","banana","litchi"]
# list2=["mango","banana","litchi"]
# list3=list1
# print(list1 is list3)


# split method - split the string in lists separated by commas or spaces

# name,age="anjali 34".split()
# print(name,age)

# join method - split the lists into string with which , or space
# user=" ".join(["anjali","23"])
# print(type(user))

# looping in lists 

# list1=["anjali","23"]
# for item in list1:
#     print(item)

# list inside list 
matrix=[["apple","mango"],["brinjal","onion"],[2,3,4]];
# # print(matrix[0][1])
# for i in matrix :
#     for j in i:
#         print(j)


# values access 
# print(matrix[1][1])



# generate list with range function

# even = list(range(2,11,2))
# print(even)


# index method 
# print(mixed.index("mango"))


# list=[1,2,3,4,5];
# neg=[]
# def negative(l):
#     for i in list :
#         neg.append(-i)
#     return neg
# print(negative(list))

# square=[]
# def squre(l):
#     for num in l:
#         square.append(num**2)
#     return square
# print(squre(list))


# reverse the number 

# num=[1,2,3,4,5]
# num2=num.copy()
# rev = []
# for i in num :
#    rev.append(num2.pop())

# print(rev)


# words reverse in a list 

# alpha=['abc','def','ghi']
# rev =[]
# for i in alpha:
#    str=""
#    for j in range(-1,-(len(i)+1),-1):
#     str+=i[j]
#    rev.append(str)
# print(rev)


# def oddeven(l):
#     odd=[]
#     even=[]
#     new=[]
#     for i in l:
#         if i %2==0:
#             even.append(i)
#         else:odd.append(i)
#     new.append(odd)
#     new.append(even)
#     return new
# print(oddeven([1,2,3,4,5,6,7,8,9,10]))


# l1=[1,2,3,4]
# l2=[3,4,5]
# commanel=[]
# def comman(l1,l2):
#     for i in l1:
#         if i in l2:
#             commanel.append(i)
#     return commanel
# print(comman(l1,l2)) 


# min max function

# list1=[2,22,18,0,222]
# print(max(list1))
# print(min(list1))


list1=[1,2,3,[5,6,7],[2,3,4]];
sum=0
for i in list1:
    if type(i)==list:
        sum+=1
print(sum)
    