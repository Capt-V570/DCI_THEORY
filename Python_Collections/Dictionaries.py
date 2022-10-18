########################
##### DICTIONARIES #####
########################

## What are dictionaries?

"""
- a container with information with key/value pairs 
- consist of key value pairs
"""

fruit_colors = {
    "apple": "red",
    "berries": "blue"
}

# print(fruit_colors["apple"])
# fruit_colors.apple (dot notation, not supported in Python)

# this crashes the program
# print(fruit_colors["DOES NOT EXIST"])

# to avoid a crash, use a method like .get()
# print(fruit_colors.get("X"))
# print(fruit_colors.get('apple'))

# # .get() method takes an optional extra argument that defines the default value
# print(fruit_colors.get('x', 'Yellow'))

# You can iterate over dictionaries
fruit_colors = {
    "apple": "red",
    "berries": "blue"
}
# print(color)
# study: Lists
# for color in fruit_colors:
#     print(f"The color of {color} is {fruit_colors.get(color)}")
#     print(f"The color of {color} is {fruit_colors[color]}")

# print(fruit_colors.keys())
# for k in fruit_colors.keys():
#     print(k)

# print(fruit_colors.values())
# for v in fruit_colors.values():
#     print(v)

# print(fruit_colors.items())
# for a_tuple in fruit_colors.items():
#     # print(a_tuple)
#     # "unpacking"
#     x, y = a_tuple
#     print(x)
#     print(y)
#     print("=" * 10)

# for x, y in fruit_colors.items():
#     print(x)
#     print(y)
#     print("=" * 10)


# Puzzle
# "DATABASE"
d = {
    "soccer": "played with a ball",
    "paddle": "Fake tennis",
    "poker": "played in vegas"
}

# delete a key that ends with `er` 
# use existing dictionary methods 
# make a copy of the dictionary

# for k in d.fromkeys(d.keys(), ''):
#     if k.endswith('er'):
#         del d[k]

# general - agnostic!
# what error do you get?
# for k in d:
#     if k.endswith('er'):
#         # del d[k] # d.pop(k)
#         d.pop(k)
# ​
# print(d)        

# How we fix the error above: for k in d.copy()
# ​
# Common methods you will work with in dictionaries
# - .copy() - returns a copy of the dictionary
# - .get(x, default) - gets the value of x where x is a key in the dictionary (or not), otherwise returns default
# - .items() - gets an iterable of key, value pairs as a tuple.
# - .keys() - get an iterable of keys in a dictionary
# - .values() - get an iterable of values in a dictionary​

list_of_days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

# designing a calendar system for humans!! (programmers count from zero, but humans do not)
# "Monday is day 1", Tuesday is day 2, etc.
# for index, day in enumerate(list_of_days):
#     print(f"{day} is day {index + 1}") # Note -> index adjusted to increase value by 1.

# this is another way of using enumerate
# for index, day in enumerate(list_of_days, start=1):
#     print(f"{day.capitalize()} is day {index}")

# zip -- combining two iterables to produce an object (combined)

# x = [1,2, 3, 4]
# y = ['a', 'b', 'c', 'd']
# # p = ['x', 'y', 'z', 'q']
# z = zip(x, y)
# print(dict(z))
# print(z)
# for i in z: 
#     print(i)
# d = dict(z) # creating a dictionary from 2 different lists
# print(d)
# for i in z:
#     print(i)
# "not dictionary"
# print(z)
# print(type(z))


x = [1,2, 3, 4]
y = ['a', 'b', 'c', 'd']
# [ (1, 'a'), (2, 'b')]
# print(zip(x, y))
# for (a, b) in zip(x, y):
#     # print(j)
#     print(a, b)
# print('*****')
# for (index, value) in enumerate(x):
#     print(y[index], x[index]) # x[index] == value 

# Max versus Min
numbers = [3, 1, -4, 2,4,4,4,4,4,4,4,4,4,4,4,100, 5] # 100 

# for loop to get hundred
# max_value = 0
# for n in numbers: 
#     if n > max_value:
#         max_value = n
# max_value = max(numbers)
# min_value = min(numbers)
# print(max_value)
# print(min_value)


# words = ["apple", "aaaaple", "cat", "caaat"]
# print(min(words))

numbers = [3,2,1]
# numbers.sort() # warning! (returns None, but sorts the global entity)
# numbers = sorted(numbers) # sorts and returns the sorted list but does not change the original list
# sorted(numbers)
# print(numbers)

# numbers = sorted(numbers, reverse=True)
# print(numbers)

# numbers.sort(reverse=True)
# print(numbers)

# d = { 'c': 2, 'b': 1, 'a': 3}
# print(sorted(d)) # default sorting is by key.
# print(sorted(d.keys())) # sorting where we specify keys
# print(sorted(d.values())) # sorting by values 
# print(d)

# books = [
#     {"cost": 10, "name": 'Python 2'},
#     {"cost": 1, "name": 'Best tourism sites in Napoli'},
#     {"cost": 5, "name": 'Basket Weaving for Pros'},
#     {"cost": 8, "name": 'Java for dummies'},
# ]
# # print(sorted(books, key=lambda book: book['cost']))

# # readable!
# func = lambda book: book['cost']
# print(sorted(books, key=func))







'''

fruit_colors = {
    "banana": "yellow",
    "cherry": "red",
    "kiwi": "green"
    }


# how to extract a value from a key of the dictionary:
print(fruit_colors["banana"])       



# how to unpack a dictionary:

# - version 1 (unpacking keys):

for k in fruit_colors.keys():
    print(k)

# - version 2 (unpacking values):
for v in fruit_colors.values():
    print(v)

for a_tuple in fruit_colors.items():
    print(a_tuple)
    # doing the unpacking:

for a_tuple in fruit_colors.items():
    print(a_tuple)
    # doing the "unpacking":
    x, y = a_tuple
    print(x)
    print(y)
    print("*" * 10) # divisore

# doing the "unpacking" directly at beginning of for loop :
for x, y in fruit_colors.items():
    print(x)
    print(y)
    print("*" * 10) # divisore


# remove keys that ends with a specific suffix:

d = {
    "soccer": "something",
    "hokey": "somethingelse",
    "poker": "otherthing"
}

for k in d.copy():
    if k.endswith("er"):
        del d[k]                         

print(d)
'''

#### BASIC COLLECTION - LISTS (again) #####
# design a calendar system for humans!! (as for the fact that programmers count from zero (0), but humans do not!)
# e.g.: Monday is day 1, Tuesday is day 2, etc.
# So, given a list, unpack it and enumerate it:

list_of_days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

# version 1
for index, day in enumerate(list_of_days):            # create for loop to unpack list and enumerate the list items
    print(f"{day.capitalize()} is day {index + 1} of the week\n")     # print in a formatted string (f-string) the Days of the week (capitalized) changing the indexing to a humanistic way

# version 2
for index, day in enumerate(list_of_days, start=1):            # create for loop to unpack list and enumerate the list items, starting from number 1 directly =)
    print(f"{day.capitalize()} is day {index} of the week\n") 


# zip -- meaning: combining two iterables to produce an object (combined)

x = [1, 2, 3]
y = ["a", "b", "c"]

z = zip(x, y)
for i in z:
    print(i)

print("*" * 20)

# creating a dictionary out of a 'zip'

x = [1, 2, 3]
y = ["a", "b", "c"]
z = zip(x, y)
d = dict(z)
print(d)