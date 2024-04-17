a,b=input("enter two number to perform division ").split(" ")

def divide(a,b):
    try:
    
        print(int(a)/int(b))
    
    except ZeroDivisionError :
        print("cannot divide by zero ")
    except ValueError :
        print("both the numbers should be in integer")
    except:
        print("something is wrong ... enter correct input")


divide(a,b)