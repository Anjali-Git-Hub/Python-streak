# evens=[2,9,6,8,10]


# print(any([i%2==0 for i in evens]))


# exercise 

def add(*args):
    if (all([type(i)==int or type(i)==float for i in args] )):
        sum=0
        for i in args:
            sum+=i
        return sum
    else:
        return "false input"

print(add(1,2,3,3,0,0))