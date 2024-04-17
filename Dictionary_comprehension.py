# {1:1,2:4,3:9}

# square={num:num**2 for num in range(1,11)}

# print(square)

# {a:2,n:1,j:1,l:1}
# name="Anjali li"
# word_count={i.lower():name.lower().count(i.lower()) for i in name}
# print(word_count)

# odd even 
# {1:"odd",2:"even"...}

odd_even={num:("even" if num%2==0 else "odd") for num in range(1,11)}
print(odd_even)