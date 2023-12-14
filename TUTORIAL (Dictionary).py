# Dictionaries
band = {
    "vocals": "Plant",
    "guitar": "Page"
    }

band2 = dict(vocal= " plant", guitar= "Page")
print(band)
print(type(band))
print(len(band2))
print(band2)
#Access items on dictionary
print(band["vocals"])
print(band.get("guitar"))

#list all keys and values
print(band.keys())
print(band.values())

#list of key/values pairs as tuples
print(band.items())

#Verify a key exists
print("guitar" in band)
print("angular" in band)

#change values
band["vocals"] = "Coverdale"
print(band)
band.update({"bass":"JPJ"})
print(band)

#Remove items
band.pop("bass")  
print(band)

band["drums"] = "Bonham"
print(band)
print(band.popitem()) #tuple
print(band)

#Delete and clear
band["drums"] = "Bonham"
print(band)
del band["guitar"]
print(band)

band2.clear()
print(band2)

del band2

'''
#Copy dictionaries
band2 = band #create a reference
print("Bad copy!")
print(band2)
print(band)


band2["drum"]="Dave"
print(band)
'''
band2 = band.copy()
band2["drum"] = "Dave"
print("Good copy!")
print(band)
print(band2)

# Or use the dict() constructor function
band3 = dict(band)
print("Good Copy!")
print(band3)

member1 = {
    "name" : "Plant",
    "Instrument" : "vocals"
}

member2 = {
    "name" : "Page",
    "Instrument" : "guitar"
}

band = {
    "member1" : member1,
    "member2" : member2
    }
print(band)
print(band.get("member1"))
print(band['member1']['name'])
print("")*2


#SETS

nums = {1,2,3,4}
nums2 = set((1,2,3,4))
print(nums)
print(nums2)
print(type(nums2))
print(len(nums2))

# No duplicate allowed
nums = {1,2,2,3}
print(nums)

# True is a dupe of 1, False is a dupe of zero
nums = {1, True, 2, False, 3, 4, 0}
print(nums)

# To check if a value is in a set
print(2 in nums)

# Buh you cannot refer to an element in the set with an index
# position or or a key
   
# Add a new element to a set
nums.add(8)
print(nums)

# Add elements from one set to another
morenums = {5, 6, 7}
nums . update(morenums)
print(nums)

# NOTE: You can use update with lists, tuples, and dictionaries too.

# Merge two sets to create a new set
one = {1,2,3}
two = {5,6,7}

mynewset = one.union(two)
print(mynewset)

# Keep only the duplicate
one = {1,2,3}
two = {2,3,4}
one.intersection_update(two)
print(one)

# Keep everything except the duplicate
one = {1,2,3}
two = {2,3,4}
one.symmetric_difference_update(two)
print(one)



