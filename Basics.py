# print("hello")
# print('im anjali')  
# print("i'm anjali")
# # print('i'm anjali')  not allowed 

# # we can use escape characters

# print('i\'m anjali')

# # escape sequences as a normal text

# print("this is new line comment \\n ")
# print("this is double backslash \\\\")


# print("\\\" \\\'")

# print("this is \\\\ double backslash")
# print("these are mountains /\\/\\/\\")
# print("he is \t awesome")
# print("\\\" \\n \\t \\\'")

# # trick

# print(r"this is \n new line ")


# # operators
# print(3/4)
# print(3//4)
# print(3%4)
# print(3**2)
# print(12.5%6)
# print(2**2**1)


# # string formatting 
# # python 2
# # python 3
# # python 3.6

# # python 3
# print("my name is {} and my age is {}".format("anjali",5))

# python 3.5
name ="anjali"
age=2
# print(f"my name is {'anjali'} and my age is {age}")

# ex1
# num1,num2,num3=input("Enter 3 number separated by blank space ").split()
# print(f"the avarage of the numbers is {(int(num1)+int(num2)+int(num3))/3}")

#string slicing

# print(name[-1:3:-1])


# ex2
# name=input("enter your name ")
# print(name[::-1])

# print(len(name))
# # methods and functions of string
# # lower upper count 
# # print(name.lower().count('a'))

# # title()
# print(name.title())

# name="             anjali              "
# print(len(name))
# name =name.strip()
# print(len(name))

sentence =" hello world i am anjali and i am 5 years old i am happy"

# replace method 
# print(sentence.replace(" ","_"))
# print(sentence.replace("am","was",2))


# find method is used to find the position of a character or a word 
# pos=sentence.find("am")
# print(sentence.find("am",pos+1))


