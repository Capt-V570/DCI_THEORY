##################
##### TUPLES #####
##################

# Tuples cannot be mutated, 
# however there are some situation, e.g. 

x = ( [], )

# adding to a data structure that can change
x[0].append("works")

# Converting from a tuple to a list
# pass the tuple to the list constructor
x = list(x)

# deduplication with a word:
word = "this worrd has many words with duplicates"
counts = {}

for char in word.lower():
    counts.setdefault(char, 0)
    counts[char] = counts[char] + 1


# same thing using a 'set':
# (Refer to the "word" variable above!)
counts = {}
for char in set(word.lower()):
    counts.setdefault(char, 0)
    counts[char] = counts[char] + 1




##### ADD items in a set: 

# In [13]: locations = { "Berlin" }

# In [15]: locations.update("Napoli", "Hamburg", "Sydney", "New York")

# In [16]: print(locations)
# {'m', 'S', 'i', 'k', 'a', 'r', 'g', 'p', 'w', 'e', 'Y', 'b', 'H', ' ', 'o', 'y', 'N', 'Berlin', 'u', 'l', 'd', 'n'}

'''
In [17]: locations.add("Napoli", "Hamburg", "Sydney", "New York")
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-3a627dfa9647> in <module>
----> 1 locations.add("Napoli", "Hamburg", "Sydney", "New York")

TypeError: set.add() takes exactly one argument (4 given)
'''

# In [18]: locations.add("Napoli",)

# In [19]: locations.add("Hamburg",)

# In [20]: locations.add("Sydney",)

# In [21]: locations.add("New York",)

# In [22]: print(locations)
# {'m', 'S', 'Napoli', 'Sydney', 'i', 'k', 'a', 'r', 'g', 'p', 'w', 'e', 'Y', 'b', 'H', ' ', 'o', 'Hamburg', 'y', 'N', 'New York', 'Berlin', 'u', 'l', 'd', 'n'}


locations = {"Berlin", "Munich", "Stockhom", "Barcelona"}

# locations.update({'Tokyo'})
# locations.update(['Beijing', 'Tokyo'])
# print(locations)

# locations.pop()
# locations.remove("Berlin")
# locations.discard("Berlin")
# locations.discard("Munich")
# print(locations)
# locations.clear()
# print(locations, "After")
# copy_location = locations.copy()
# print(copy_location)

A = { 1, 2, 3, 4}

B = { 5, 6, 7}

# email marketing campaign
# Container A -> incomes < 1500 euro; Container B -> 1500 euro 
# print(A.intersection(B))
# print(A.difference(B))
# print(B.difference(A))

# symmetric difference (XOR) # Logical thinking 
# print(A.symmetric_difference(B)) # removes the intersection
# print(A, B, 'before')
# print(A - B, 'What is the intersection?')
# print(A.intersection(B), 'What is the intersection?')
# B.intersection_update(A)
# print('A:', A, 'B:', B, 'after')
# print(A.difference(B))
# print(B.difference(A))

# print('A: ', A, 'B: ', B)
# A.symmetric_difference_update(B)

# print(B.symmetric_difference_update(A))
# print('A: ', A, 'B: ', B)
print(A.union(B))
print(A)
print(B)

# website - membership plans (Basic, Premium, Pro)
# Reminder or promotion email 
# A = [1,2,3,4] # 
# B = [4,5, 6, 7]
# print(A+B) # send emails, duplicate? 
# de-duplicate (removes things that show up two times)
# print(set(A).union(set(B)))

# print(A.isdisjoint(B))

list = {"Christiano",'Antony',"Lisandro","Marcus"}
# bencher = {"Antony", "Lisandro", "Christian Eriksen"}
bencher = {"Christiano",'Antony',"Lisandro","Marcus", "Giacomo", "Juan Jesus"}
print(bencher.issuperset(list))



