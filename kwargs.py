# def func(one,**kwargs):
#     print(kwargs)
#     print(one)

# di={"name":"anjali","age":4}
# func("anjali",**di)


# padk

def func (*args,**kwargs):
    if "True" in kwargs.values():
       return  [i[::-1].title() for i in args ]


print(func(*["anjali","li"],reverse_str="frue"))


