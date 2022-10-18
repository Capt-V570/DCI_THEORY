###############################################################
###### Theory on Basics - Collection (October 7th, 2022) ######
###############################################################

fridge = [
 "Apple", "Apple", "Cabbage",
 "Steak", "Cheese", "Apple",
 "Carrot", "Carrot", "Iogurt",
 "Beer"
]

counter = {}

for ingredient in fridge:
    if ingredient not in counter:
        counter[ingredient] = 0
    counter[ingredient] += 1

print(counter)



#########################
###### Costructors ######
#########################

'''
Class constructors are a fundamental part of object-oriented programming in Python. 
They allow you to create and properly initialize objects of a given class, making those objects ready to use.
'''
