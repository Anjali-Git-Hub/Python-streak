# l=[1,2,22,33,1,2]
# names=["anjali","komal","rajni","yash"]
# print(max(names,key=lambda name:len(name)))

details=[
    {"name":"anjali","age":3,"score":300},
    {"name":"yashika","age":13,"score":100},
    {"name":"anja","age":3,"score":200},

]

print(min(details,key=lambda obj:obj['score']))

# print(max(l))
# print(min(l))

# l=[
#     {"prod":"tv","price":1600},
#     {"prod":"iphone","price":2600},
#     {"prod":"ipad","price":600},

# ]

# print(min(l,key=lambda d:d['price'])['prod'])


# names=["anjali","koaml","been"]
# print(max(names,key=lambda i:len(i)))