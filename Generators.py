# generators are iterators

# def nums(n):
#     for i in range(1,n+1):
#         print(i)
# nums(6)
# for i in gen:
    # print(i)

# for i in gen:
#     print(i)

# def gen(n):
#     return (i for i in range(1,n+1) if i%2==0)

# for i in gen(4):
#     print(i)

# list vs generator
import time

# gen=(i**3 for i in range (1,1000000))
t1=time.time()

l=[i**3 for i in range (1,1000000)]
print(time.time()-t1)


