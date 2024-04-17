class circle:
    # class variable
    pi=3.14
    def __init__(self,radius):
        self.radius=radius
    def circumference(self):
        return 2*circle.pi*self.radius
    def area(self):
        return circle.pi*(self.radius**2)


c1=circle(4)
print(c1.circumference())
print(c1.__dict__)
print(c1.area())