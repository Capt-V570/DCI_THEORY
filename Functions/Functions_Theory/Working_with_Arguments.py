#####################################################
############# Working with Arguments ################
#####################################################


def full_name(*args): # "tuple" ("sdkdfhsdkjf", "sdkjfhsdkhf")
    # 2 names, 3 etc.
    # Handle it "gracefully!!"
    # print(args)
    # return f"{args[0]} {args[1]} {args[2]} {args[3]}"
    # --> TUPLE / List (Tuples cannot be changed/mutated )
    return args

# looping crash
names = ('Felipe', 'Gonzalez') ## tuple

# 2 major ways of doing it
full_string = ""
for name in names:
    full_string += f"{name} " # name + " " $$$
    # print(name, end="") # A for effort!!!

print(full_string.strip())    


print(full_name("A", "B", "C"))
print(full_name("A", "B"))
print(full_name("A"))
'''
print(full_name("Diego", "Armando", "Maradona"))
print(full_name("Diego", "Maradona"))
print(full_name("D10S"))
'''

d10s = ("Diego", "Armando", "Maradona", "D10S")
for args in d10s:
    full_name += f"{args[0]} {args[2]} is {args[3]}" 
    print(full_name())


