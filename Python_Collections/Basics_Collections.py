##################################################################
###### Theory on Basics - Collection (September 30th, 2022) ######
##################################################################

# In [1]: string
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-1-edbf08a562d5> in <module>
# ----> 1 string

# NameError: name 'string' is not defined

# In [2]: string = "Berlin"

# In [3]: string
# Out[3]: 'Berlin'

# In [4]: string = list(string)

# In [5]: print(string)
# ['B', 'e', 'r', 'l', 'i', 'n']

# In [6]: string[0] = "C"

# In [7]: string
# Out[7]: ['C', 'e', 'r', 'l', 'i', 'n']

# In [8]: full_string = ""

# In [9]: for s in string:
#    ...:     full_string += s
#    ...: 

# In [10]: print(full_string)
# Cerlin

# In [11]: 

# In [11]: list("autobots")
# Out[11]: ['a', 'u', 't', 'o', 'b', 'o', 't', 's']

# In [12]: transformer = list("autobots")

# In [13]: print(transformer)
# ['a', 'u', 't', 'o', 'b', 'o', 't', 's']

# In [14]: full_word = ""

# In [15]: for s in transformer:
#     ...:     full_word += s
#     ...: 

# In [16]: print(full_word)
# autobots

# In [17]: print(transformer)
# ['a', 'u', 't', 'o', 'b', 'o', 't', 's']

# In [18]: transformer[0].join()
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-18-2db0da0097ec> in <module>
# ----> 1 transformer[0].join()

# TypeError: str.join() takes exactly one argument (0 given)

# In [19]: "".join(trasformer)
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-19-22fe9ff21c50> in <module>
# ----> 1 "".join(trasformer)

# NameError: name 'trasformer' is not defined

# In [20]: "".join(transformer)
# Out[20]: 'autobots'

# In [21]: sequence = range(1, 5 , 2)

# In [22]: print(sequence)
# range(1, 5, 2)

# In [23]: print(list(sequence))
# [1, 3]

# In [24]: s = range(1,5)

# In [25]: list(s)
# Out[25]: [1, 2, 3, 4]

# In [26]: range(1, 4.5, 0.1)
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-26-1f7cdee76de1> in <module>
# ----> 1 range(1, 4.5, 0.1)

# TypeError: 'float' object cannot be interpreted as an integer

# In [27]: help(range)







# Study from Module 2 - Python Programming // Python Collection Slides

# Exercise:

lists = [ ["John",[ {"name": "Mary"} ], "Amy"], [ 32, 43,{'age': 100}, 51] ]

'''
Print the value of Mary
Print the age of 100.
'''

# Output:

print(lists[0][1][0]["name"])
print(lists[1][2]["age"])


# RANGE:

sequence = range(1, 5, 2)

print(sequence)

print(list(sequence))

s = range(1,5)

list(s)

# Lists: Accessing Values

#### SORTING ####

# Reverse:

words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']

words.reverse()             # proper way to use this method: using it by itself - without re/assigning it to any variable (otherwise returns 'None')

print(words)


# Sort:
words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']

#words = words.sort()       # doing this, will just return 'None' in CLI
words.sort()                # this is the proper way how to use this method (likewise to the method 'reverse()')

print(words)


# NOTE: Playing around:

words.sort(reverse=True)    # this will sort AND reverse at the same time

print(words)

# Remove Replace:

words = ['cat', 'aadvark', 'elephant', 'squirrel', 'hippo']

words[1:3] = ["lion"]       # this, will 'slice' the list and replace these items from [1:3] with the single item 'lion'
#words[3] = "lion"          # this, will only replace position 3 in the list with 'lion' - not useful for this scope

print(words)