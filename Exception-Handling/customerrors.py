class clubEntry(ValueError):
    pass


age=int(input("Enter your age "))
if age>=18:
    print("welcome to phonix club")
else:
    raise clubEntry("You are not welcomed !!")