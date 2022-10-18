'''
As of today we know primitive data types have we seen?

- strings
- integer
- float
- boolean

----------
Compound data type
---------
- Lists
- Tuples


'''

# What is a tuple?

# it is an ordered sequence of elements, can mix element types of data. e.g.:

name = ("Miri", "Lucas")
other_name = ("Peer", "Hoffman")

# tuples (are immutable)

name = name + other_name
# print(name)

numbers = (1,2,3,4,5,6,7,8,9)
print(numbers[0:1]) # 2, 3, 4, 5

# inbuilt "len" function/method
print(len(numbers))
print(numbers[0])

# negative indexing
print(numbers[-2])

# playing around with tuples:

print(numbers[:3])
print(numbers[3:6])

# negative indexing
print(numbers[-3:-1])
print(numbers[0:-3])





# quotient and remainder 

'''
Check the recording tostudy this again
'''






# given these following examples:
x = 45
y = 50

# can you swap the values?
print(f"x->{x}, y=> {y}")
temporary_store = x
x = y
y = temporary_store
print(f"x->{x}, y=> {y}")

# swap in python
(x, y) = (y, x)
print(f"x->{x}, y=> {y}")

'''
Design a function that takes in a gender and a first name and a last name 
If the gender is male return a greeting with (Good morning Mr. <fist name>) and a full name 
If the gender is " female", return a greeting (Good morning Ms. <first name>)
'''

def greeting_fullname(first_name, last_name, gender):
    greeting = ""
    full_name = f"{first_name} {last_name}"
    if gender == "male":
        greeting = f"Good Morning Mr. {first_name}"
    else:
        greeting = f"Good Morning Ms. {first_name}"
    return (greeting, full_name)

# test case
print(greeting_fullname("Fausto", "Ferrara", "male"))
print(greeting_fullname("Flavia", "Ferrara", "female"))


# option with a 3rd unknown gender:

def greeting_fullname(first_name, last_name, gender="Mr./Ms."):
    full_name = f'{first_name} {last_name}'
    greeting = ''
    if gender == 'male':
        greeting = f"Good morning Mr. {first_name}"
    elif gender == 'female':
        greeting = f"Good morning Ms. {first_name}"
    else:
        greeting = f"Good morning {gender} {first_name}"
    return (greeting, full_name)

# test case: 

print(greeting_fullname("Ajeje", "Brazov", "unknown"))


# What is an Iteration?
# Iteration is going through each and every element of a collection

sizes = ("S", "L", "M", "XL","XS", "L", "M", "XXL","S", "L", "M", "XXL","S", "L", "M", "XXXL")

for s in sizes:
    print(s)
    #print(sizes[0])


# What is a list? 
# A list is a Ordered sequence of Information that are accessible by an index
# we denote by the use of squared brackets -> [ ]
# list contains elements that can be mixed data types (not common/ not encouraged) and pure and homogeneous data types
# "m" word?? Lists are Mutable! (= lists are changeable)

sizes = ["xs", "m", "l", "xl", "xs"]
print(len(sizes))
#access items in a list
print(sizes[0])

i = 100
print(sizes[i - 99]) # will return item at position 1 (=m)



# Now, design a While loop:
sizes = ['l','m', 'xl', 'xxl']
s = 0 # counter variable
# > , < , <=, >=
while s < len(sizes): # 99.9% WHILE [CONDITION -has to be true]:
    print(sizes[s])
    s += 1


# To get a total, we have a function that looks like this, rewrite (refactor) the function to use a while loop

def total_list(lst):
    total = 0
    for item in lst:
        total += item
    return total

# test case
print(total_list([1,2,3]))   # answer is 6


def total_list(lst):
    total = 0
    # counter variable
    index = 0
    while index < len(lst):
        total += lst[index]
        index += 1
    return total

# test case
#print(total_list_while([1,2,3]))   # answer is 6
print(total_list([1,2,3]))         # answer is 6