##############################################################
############# FUNCTIONS THEORY (11 OCTOBER 2022) #############
##############################################################

"""
RECURSIVE FUNCTIONS:

- What are recursive functions?

- Recursive Functions are functions that call themselves!

"""

# def func():
#     func()
# rules?
# Have a base case - have a place to stop this function from calling itself
# mathematics!
# factorial method
# e.g. 3!
# 3 x 2 x 1 x (0!), in math the symbol, !, is used to mean factorial
# the base case here is 0, at which point the function returns 1.

def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


# Python supports up to 1000 frames in its recurrsion limit, 
# this can be raised as shown below

# import sys
# sys. setrecursionlimit(5000)
# 3 x 2 x 1 x 0! -> 6
# for i in range(2000):
#     print(factorial(i), f'i->{i}')

# fibonacci - famous for the fibonnaci sequence
# Rabbits
# 1, 1, 2, 3, 5, 8, 13

# add the sum of numbers in a list?
x = [1, 2, 3]

# 20 minutes, trying to rewrite this to use a recursive style
def get_sum(list):
    total = 0
    for i in list:
        total += i
    return total

# here we total up values from the end of the list to the beginning
# def pascos_sum(list):
#     print(list)
#     if len(list) == 0:
#         return 0
#     return list[-1] + pascos_sum(list[:-1])

# print(pascos_sum([1,2,3]))

# here we are totaling from the beginning of the list
def sum_list(lst):
    if not lst:  # is the list empty?
        return 0
    else:
        # extract one value from the list (and reduce)
        first = lst.pop(0)  # reduces the list and also stores the value to use
        return first + sum_list(lst)  # lst -> mutating


print(sum_list([1, 2]))  # 3

# iterative solutions can be done in a recursive way 
# (i.e. if you are able to write it using a loop, you can also do it in a recursive way)
names = ["victor", "peer", "pasco"]
# for name in names:
#     print(f"Hello {name}")

# def recursive_greet(names):
#     if not names: # base case
#         return "finito"
#     else:
#         print(f"Hello {names.pop()}")    # reduction of the list
#         return recursive_greet(names)

# print(recursive_greet(names))

# Some times you have to write a function in a function

# def outter_function():
#     x = "I am a variable"
#     def inner_function():
#         def inner_inner_function():
#             return "I am also hidden"
#         print("I am an inner function")
#         inner_inner_function()

#     return inner_function()

# scoping rules
# inner_function()
# print(x)
# print(outter_function())

# nested function


# def outer(x):
#     def inner(y):
#         print('y is here')
#         return y

#     print(inner("Fausto"))
#     return x

# print(outer('Doe'))
# make the code readable
# def outer(x):
#     def add_mr_miss(y):
#         return f'Mr/Ms {y}'
#     return add_mr_miss(x)

# print(outer('Doe'))

# passing a function as an argument


def do_something(string, func):
    return func(string)


def add_a_greeting(name):
    return "Good morning " + name


def make_upper(name):
    return name.title()


# functional (paradigm)
print(do_something("peer", make_upper))
capital_value = do_something("peer hoffman", make_upper)
print(do_something(capital_value, add_a_greeting))
# or
print(do_something(do_something("peer hoffman", make_upper), add_a_greeting))
# print(do_something('peer', add_a_greeting))


'''
def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        # expensive (your computer might crash)
        return n * factorial(n - 1)

print(factorial(3))
for i in range(1000):
    print(factorial(i), f"i->{i}")
'''



# 20 minutes, trying to rewrite this to use a recursive style:
'''
def get_sum(list):
    total = 0
    for i in list:
        total += i
    return total

# version 1:
def get_sum(list):
    #print(list)
    if not list:
        return 0
    else: 
        first = list.pop(0)
        return first + get_sum(list)
'''
# version 2:
def get_sum(list):
    print(list)
    if len(list) == 1:
        return list[0]
    else: 
        first = list.pop(0)
        return first + get_sum(list)
'''
# version 3 - ask pasco: Negative Slicing:
def get_sum(list):
'''

numbers = [1,2,3]

print(get_sum(numbers))