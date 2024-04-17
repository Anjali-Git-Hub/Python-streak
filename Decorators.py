# # decorators are the functions that will decorate other function 

# # from functools import wraps
# # def decorator(function):
# #     @wraps(function)
# #     def wrapper(*args):
# #         ''' Inside wrapper function '''
# #         print("adding two numbers")
# #         return function(*args)
# #     return wrapper
# # @decorator
# # def add(a,b):
# #     ''' function to add two number '''
# #     return a+b

# # print(add(1,2))
# # print(add.__doc__)
# # print(add.__name__)

# import time
# def calculateTime(function):
#     def wrapper(*args):
#         print("time calculation...")
#         t1=time.time()
#         print(t1)
#         returned_val= function(*args)
#         t2=time.time()
#         print(f"It tooks {t2-t1}")
#         return returned_val
#     return wrapper

# @calculateTime     
# def finder(n):
#     return [i**2 for i in range(1,n)]

# finder(11)





from functools import wraps
def to_check_dtype(dtype):
    def decorator(function):
        @wraps(function)
        def wrapper(*args):
            check=[]
            for i in args:
                check.append(type(i)==dtype)
            if all(check):
                return function(*args)
            else:
                return "invalid datatype"
        return wrapper
    return decorator
@to_check_dtype(int)
def add(*args):
    add=0
    for i in args:
        add+=i
    return add
print(add(2,3,4,4,5,[2,3]))


            




