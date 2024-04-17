# avoid to use / increases complexity of code 


class A:
    def __init__(self):
        pass
    def a(self):
        print("inside a class")
    def comman(self):
        print("comman method inside A class")

class B:
    def __init__(self):
        pass
    def b(self):
        print("inside b class")
    def comman(self):
        print("Comman method in class b")


class C(A,B):
   pass


instance_of_c=C()
# instance_of_c.a()
# instance_of_c.b()

# instance_of_c.comman()


# print(C.__mro__)

