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



class fledge(smartPhone):
    def __init__(self,name,model,price,camera):
        super().__init__(name,model,price,camera)





nokia=smartPhone("nokia","nokia 223","40000","10 MP")
# print(nokia.__dict__)

samsung=fledge("samsung","samsung13",67889,"10 MP")
# print(samsung.details())
# print(help(fledge))

# isinstance and issubclass()
# print(isinstance(samsung,fledge))
# print(isinstance(nokia,fledge))
# print(issubclass(fledge,Phone))






