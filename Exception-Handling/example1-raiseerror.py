class Phone :
    def __init__(self,name) :
        self.name=name
class SmartPhones:
    def __init__(self) :
        self.phones=[]
    def addPhones(self,newPhone):
        if isinstance(newPhone,Phone):
            self.phones.append(newPhone)
        else :raise ValueError("Not added .....")

samsung=Phone("samsung")
Android = SmartPhones()
# Android.addPhones(samsung)
# print(Android.phones[0].name)

Android.addPhones("oneplus 12")
