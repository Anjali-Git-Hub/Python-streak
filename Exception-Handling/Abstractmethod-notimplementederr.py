# in python we dont have any thing like abstract method but in java programming there are abstract method concept
# but in python we can implement abstract methods by using 
# NotImplemented error


class Phone:
    def __init__(self):
        pass
        # every phone has there different outlines , highlights or we can say 
        # every phone has their own details 

#abstract method 
    def fullDetail(self):
        raise NotImplementedError("please create your own method for details ")

class Android(Phone):
    def __init__(self):
        super().__init__()
    
samsung=Android()
samsung.fullDetail()