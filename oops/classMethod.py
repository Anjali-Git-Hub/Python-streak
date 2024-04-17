class Person:
    # this decorator will deorate this method by automatically passing the class in this method
    @classmethod
    def class_method(cls):
        print(f"This is class method {cls.class_method} of class {cls.__name__}")
Person.class_method() 

