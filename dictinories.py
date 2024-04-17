# creating dictionary
# user={"name":"anjali","age":23}
# print(user)

# user1= dict(name="anjali",age=2)
# print(user1)

# user2={}
# user2['name']="anjali"
# user2['age']=5
# print(user2)

# moreinfo={"country":"india","relationship_status":"always single only!!"}
# user2.update(moreinfo)
# print(user2)

# user={"name":"anjali","age":23}
# looping 
# for key,value in user.items():
#     print(key,value)

# dict_items=user.items()
# print(dict_items)


# methods in dictionaries 
# user={"name":"anjali","age":23}

# fromkeys() method
# d=dict.fromkeys(["name","age"],"unknown")
# print(d)

# print(user['names']) -- error 
# print(user.get('names',"not found !!")) -- it is better to check 


# clear() method
# user.clear()
# print(user)


# check whether the particular value or key present in dictionary or not 
# user={"name":"anjali","age":23}
# if user.get("namess"):
#     print("yes")
# else:
#     print("no")


# delete the data from dictionary
# user={"name":"anjali","age":23}
# popped=user.popitem()
# print(popped)
# print(user)



# exercise-->

# def cube(n):
#     new={}
#     for i in range(1,n+1):
#         new[i]=i**3
#     return new

# print(cube(4))


# word counter

# def word_counter(name):
#     new={}
#     for i in name:
#         new[i.lower()]=name.lower().count(i.lower())
        
#     return new
# print(word_counter("Anjali LI"))

l=input("enter your name,age,counrty separated by commas ").split(",")
inn=["name","age","country"]
user={}
for i in range(0,len(inn)):
    user[inn[i]]=l[i]
print(user)


