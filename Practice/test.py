nums=input("enter numbers ").split(",")
print(nums)
numsint=[int(i) for i in nums]

check=[]
def removeDuplicates(l):
    for i in l:
          if i not in check:
               check.append(i)
    return check
print(removeDuplicates(numsint)) 
