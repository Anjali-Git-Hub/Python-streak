class Laptop:
    discount=40
    def __init__(self,brandname,model,price):
    
        self.brandname=brandname
        self.model=model
        self.price=price
    def apply_discount(self):
        dis_price=(self.discount*self.price)/100
        self.price=self.price-dis_price


hp=Laptop("hp","xu1004",36000)
dell=Laptop("dell","xu1005",30000)

# print(hp.__dict__)
# print(dell.__dict__)

# hp.apply_discount()
# dell.apply_discount()
# print(hp.__dict__)
# print(dell.__dict__)

# special offer 
hp.discount=100
hp.apply_discount()
print(hp.__dict__)