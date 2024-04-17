class Phone:
    def __init__(self, model, price):
        self.model = model
        if price > 0:
            self._price = price
        else:
            self._price = max(price, 0)

    @property
    def complete_specification(self):
        return f"{self.model} {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price=max(new_price,0)

nokia = Phone("nokia", -36000)
print(nokia.complete_specification)

nokia.price = -300
print(nokia.complete_specification)
