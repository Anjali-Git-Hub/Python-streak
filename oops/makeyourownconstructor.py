class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    # class method
    @classmethod
    def my_constructor(cls,s):
        fname,lname=s.split(",")
        return cls(fname,lname)

    
p1=Person("anjali","li")
# print(p1.fname)
p2=Person.my_constructor("yashi,ka")
print(p2.fname)