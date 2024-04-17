# 2 classes
# inheritance

class Phone:
    def __init__(self,name,model,price):
        self.name=name
        self.model=model
        self.price=price
    def details(self):
        return f"{self.name},{self.model}"

    
class smartPhone(Phone):
    def __init__(self,name,model,price,camera):
        super().__init__(name,model,price)
        self.camera=camera
    def details(self):
        return f"{self.name} {self.model} {self.price} {self.camera}"



nokia=smartPhone("nokia","nokia 223","40000","10 MP")
# print(nokia.__dict__)
print(nokia.details())

