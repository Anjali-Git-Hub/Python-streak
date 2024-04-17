# def add(a,b):
#     print(a+b)
# add(2,3,2,3,4,5)

# def total(num,*args):
  
#     print(args)
#     print(num)
   
# total(2,*"abc")
# 

def power(num,*args):
    if args:
         return [i**num for i in args  ]
    else:
         return "hey you didn't passed args"
        
  

print(power(2,*[1,2,3,4]))



