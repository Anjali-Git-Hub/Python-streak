class Person:
    def __init__(self,fname):
        self.__fname=fname

p1=Person("anjali") 
print(p1.__dict__)  
        
print(p1._Person__fname)

# name mangling