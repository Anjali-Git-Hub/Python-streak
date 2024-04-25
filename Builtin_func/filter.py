numbers=[2,3,4,6,7,9]


is_even=filter(lambda n:n%2==0 , numbers)
print(is_even)
for i in is_even:
    print(i)