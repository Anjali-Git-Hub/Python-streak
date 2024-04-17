

try:
    age=int(input("enter your age "))

except ValueError:
    print("you havn't passed the age is int")

except :
      print("something went wrong")
# finally:
#     print("finally clause  will always execute .........")

if age>18:
        print("you can drive")
else:
        print("you should learn cycling")