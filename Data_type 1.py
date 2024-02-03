#LIST
users = ["Dave","John","Sara"]

data = ["Dave", 42, True]

emptylist = []
print("Dave" in data) 
print("Dave" in users)
print("Dave" in emptylist)

print(users[0])
print(users[-2])

print(users.index("Sara"))

print(users[0:2])
print(users[1:])
print(users[-3:-1])

print(len(data))


users.append("Elsa")
print(users)

users = users + ["Jason"]
print(len(users), users)

users.extend(["Robert", "Jimmy", "Ade"])
print(users)

#users.extend(data)
print(users) 

users.insert(0, "Bob")
print(users)

users[4:6] = ["Eddie", "Alex"]
print(users)

users[1:3] = ["Robert", "JPJ"]
print(users)

users.remove("Eddie")
print(users)

users.pop()
print(users) 
 
del users[1]
print(users)


#del data
#print(data)


data.clear()
print(data)

users[1:2] = ["dave"]
users.sort()
print(users)

users.sort(key=str.lower)
print(users) 

nums = [4, 42, 78, 1, 5]
nums.reverse()
print(nums)

#nums.sort(reverse=True)
#print(nums)

print(sorted(nums,reverse=True))
print(nums)

numscopy = nums.copy()
mynums = list(nums)
mycopy = nums[:]
print(" ")

print(numscopy)
print(mynums)
mycopy.sort()
print(mycopy)
print(nums)

print(type(nums))

mylist = list([1,"Neil",True])
print(mylist)

#TUPLE
mytuple = tuple(('Dave',42,True))
anothertuple = (1,4,2,8,4)

print(mytuple)
print(type(mytuple))
print(type(anothertuple))

newlist = list(mytuple)
print(type(newlist))
newlist.append("Neil")
print(newlist)
newtuple = tuple(newlist)
print(newtuple)
print(newlist[1])
print(newtuple[0])

(ow, *re, gf) = anothertuple   #NOTE: it can work for list also 
print(ow, re)
print(gf)

print(anothertuple.count(4))



 



