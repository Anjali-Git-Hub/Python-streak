class Person:
    count=0
    def __init__(self):
       Person.count+=1
       pass
    def count_instance(self):
        print(Person.count)

p1=Person()
p2=Person()
p2.count_instance()
