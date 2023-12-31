import math
# String data type

# literal assignment
first = "Dave"
last = "Gray"

'''print(type(first))
print(type(first) == str)
print(isinstance(first, str))
print('')

# constructor function
pizza = ("Pepperoni")
print(type(pizza))
print(type(pizza) == str)
print(isinstance(pizza, str))
'''
#Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a number to a string
decade = str(1980) 
print(type(decade))
print(decade)

Statement = f"I like rock music from the {decade}s."
print(Statement)

# Multiple lines
multiline = '''
Hey, how are you?

I was just checking in.
                            All good?
'''
print(multiline )
# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)
print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)
print(len(multiline))
multiline += "                                       "
multiline = "                " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

# Build a menu
title = "menu".upper()
print(title.center(30,"="))
print("Coffee".ljust(16, "=") + "$1".rjust(4))
print("Muffin".ljust(16, "=") + "$2".rjust(4))
print("Cheesecake".ljust(16, "=") + "$3".rjust(4))

print('')

#string index value
print(first[0])
print(first[2:])
print(first[-2])
print(first[-4])
print(first[:-1])

# Some methods return boolean data
print(first.startswith("D"))
print(first.endswith("D"))
print(first.endswith("e"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue,bool))

# Numeric data type 
# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 3.28
y = float(1.14)
print(type(gpa))

# Complex type 
comp_value = 5 + 8j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in function for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(gpa * -1)

print(round(gpa))
print(round(gpa, 1))

print(math . pi)
print(math . sqrt(64))
print(math . ceil(gpa))
print(math . floor(gpa))

# Casting a string to a number
zip_code = "10001"
zip_value = int(zip_code)
print(type(zip_value))

zip_value = int

 