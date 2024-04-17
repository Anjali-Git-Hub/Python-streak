# nums=(1,)
# print(type(nums))

# immutable and faster than lists

nums=(1,2,3)
# print(nums.append(3))
# no append , add delete update

# nums = (1,2,3,4,["anjali","rajni"])
# nums[4].append("riyandh")
# nums[4].pop()

# print(nums)

# looping 
# for i in nums :
#     print(i)

# methods we can use with tuples
# 1. count()
# 2. len()
# 3. index()

mixed=(1,2,3,"anjali","singing")
# print(mixed.count("anjali"))
# print(len(mixed))
# print(mixed.index("anjali"))
# 

# functions we can use with tuples are 
nums=(1,2,3)
# 1. min
# print(min(nums))
# print(max(nums))
# print(sum(nums))



# unpacking tuples 
# name , age ,hobby =("anjali",9,"singing")
# print(name,age,hobby)


# function returning two values 

def two_val(num1, num2):
    add=num1+num2
    mul=num1*num2
    return add,mul

add,mul=two_val(3,4)
print(add,mul)

genratetuple= tuple(range(1,11))
print(list(genratetuple))
print(type(list(genratetuple)))



# tuple without parenthesis

singers ="arman","atif","anjali"
print(type(singers))


# slicing 
print(singers[:2])