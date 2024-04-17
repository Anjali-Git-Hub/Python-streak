class Animal:
    def __init__(self,name,type,color):
        self.name=name
        self.type=type
        self.color=color
    def greet(self):
        return f"hello {self.name}"

class Dog(Animal):
     def __init__(self,name,type,color):
         super().__init__(name,type,color)

d1=Dog("doogi","mongril","black")
print(d1.name)

print(d1.greet())
