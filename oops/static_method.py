# static methods have a logical connection with class

class Person:
    def __init__(self,fname):
        self.fname=fname
    @staticmethod
    def call_fname(self):
        print(self.fname)
        


p1=Person("anjali")
Person.call_fname(p1)