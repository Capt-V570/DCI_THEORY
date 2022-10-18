#####################################################
############# Working with Lists ####################
#####################################################

# given a list

names = ["Victor", "Peter", "Mary", "John", "Badara", "Peer"]

# using an index, replace "Peer" with "Malcom X"

index = names.index("Peer")
#print(index)
names[index] = "Malcom X"
print(names)


# Add two names to the list of names

names.insert(3, "Lucas")
names.append("Fausto")
print(names)


# Experiment with the methods in a list using dir(names)
'''
print(dir(names))
'''

names.remove("John")
print(names)

names.reverse()
print(names)

