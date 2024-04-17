


# def greatest (a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c:
#         return b
#     else:
#         return c
# print(greatest(1,2,3))

# function returning function
# def greater (a,b):
#     if a>b:
#         return a
#     return b

# def greatest (a,b,c):
#     res=greater (a,b)
#     return greater(res,c)

#     # if a>b and a>c:
#     #     return a
#     # elif b>c:
#     #     return b
#     # else:
#     #     return c
# print(greatest(5,2,3))


# is pallindrome function

check ="madam"


def pallidrome():
    new=""
    for i in range(len(check),-1,-1):
        new+=check[i]
    return new==check
      
pal