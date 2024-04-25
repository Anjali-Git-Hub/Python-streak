# 1. like __inti__


# why we use dunder or magical methods 
l=[1,2,3,4]
# print(l)
# print(len(l))

# print("anj"+"li")
# print(3+4)

class Phone:
    def __init__(self,name,model,price,camera):
        self.name=name
        self.model=model
        self.price=price
        self.camera=camera
    # str dunder is used to format the string neatly
    def __str__(self):
        return f"{self.name} {self.model} {self.price}"
    # ṛepr is used by dev for debogging and here the code is written 
    def __repr__(self):
        # can create object by copy pasting this code 9-*
        return f"Phone(\'{self.name}\',\'{self.model}\',{self.price},\'{self.camera}\')"
    def __len__(self):
        return len(self.name)
    def __add__(self,otherobj):
        return self.price+otherobj.price

p1=Phone("nokia","nokia 22",20000,"18 MP")
p2=Phone("Samsung","samsung 1200",40000,"15 MP")
print(p1)
print(p1+p2)
# print(len(p1))

# print(p1.__repr__) 

# 1. str, repr dunder method
