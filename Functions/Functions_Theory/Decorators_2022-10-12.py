#########################################################################
############# FUNCTIONS DECORATORS THEORY (12 OCTOBER 2022) #############
#########################################################################

"""
DECORATORS FUNCTIONS:

Q - What are Decorators functions?

A - Decorative Functions are functions that give additional functionality/-ies to our already existing functions!
    Without modifying the original function.

"""

# Example 1:

def outer():
    def inner():
        print("Hello, I am inner")
    return inner

o = outer()  



# Example 2:

def outer(name):
    def inner():
        print(f"Hello {name}, I am inner")
        return "Return value"
    return inner # have not executed it!!



# division case
def check_divisor(func):
    def inner(a, b):
        if b == 0:
            print("You cannot divide by 0")
            return (f"Operation is Not Possible")
        return func(a,b)
    return inner

def divide(a, b):    
    return a / b

divide = check_divisor(divide)
print(divide(4, 2))
print(divide(4, 0))


# Test Exercise: Can you create another decorator that adds the suffix “Mr/Ms” to the string?
'''
def make_title(func): # we expect the function to return a string
    def inner():
        return func().title()

    return inner        
'''
# Fausto's solution:

def make_title(func): 
    def inner(name):
        return func(name).title()

    return inner        

# use a decorator/closure
@make_title
def greetings(name):
    return f"Mr. {name}"

given_name = "fausto doe"


print(greetings(given_name))


# Victor's solution:

def make_title(func):
    def inner(name):    # the arguments of the inner function are the same arguments as the function we pass
        return func(name).title()

    return inner        

def add_mr_ms(func):
    def inner(name):
        return func(f"Mr/Ms. {name}")
    return inner

# use a decorator/closure:
@add_mr_ms      # the '@' symbols is the syntactic sugar for adding a Decorator (in Python) - NOTE: The '@' sign defines the order of which decorator will be used first!
@make_title     # NOTE: we always have to add all Decorators b4 the last function which is called first (in this case, the 1st function is: 'def greetings()')
def greetings(name):
    return name


'''


def make_title(func):
    def inner(name):
        return func(name).title()

    return inner        

def add_mr_ms(func):
    def inner(name):
        return  func(f"Mr/Ms. {name}")
    return inner

@add_mr_ms
@make_title
def greetings(name):
    return name

@make_title
def greetings(name=""):
    return f"Good morning {name}"

#additional_decorator:


'''


print(greetings("fausto doe"))




'''
VICTOR's SCRIPT BELOW

'''

# inner function


# def outer():
#     def inner():
#         print("Hello, I am inner")
#     return inner # have not executed it!!

# choice 1
# x = outer()  
# x()
# choice 2
# outer()()
# print(o)


# closure - a function returns a function

# some times closures can take in argument

# def outer(name):
#     def inner():
#         print(f"Hello {name}, I am inner")
#         return "Return value"
#     return inner # returns a value have not executed it!!

# outer('shaban')()

# division case
def check_divisor(func):
    def inner(a, b):
        if b == 0:
            print("You cannot divide by 0")
            return # stop here if there is 0. (Break in while loop?)
        return func(a,b)
    return inner

def divide(a, b):    
    return a / b

# not preferred 
divide = check_divisor(divide) # decorator used
# print(divide(4, 2))
# print(divide(4, 0))

# second (preferred)
@check_divisor
def divide(a, b):
    return a / b
# print(divide(4, 2))
# print(divide(4, 0))


# practical use-cases
# API - a way of accessing data from one location (URL (website))
# Testing of code (automation tests)
# database access
# etc.
# Application Programming Interface
# - CLI (command line interface)
# - GUI (graphical user interface)

# def make_title(func):
#     def inner(name):
#         return func(name).title()

#     return inner        

# def add_mr_ms(func):
#     def inner(name):
#         return  func(f"Mr/Ms. {name}")
#     return inner

# @add_mr_ms
# @make_title
# def greetings(name):
#     return name

# print(greetings("fausto doe"))


# def capitalize(name):
#     return f'{name.title()}'
def make_title_in_word(function):
    def inner(name): # the arguments of the inner function are the same arguments as the  the function we pass
        # print(name, 'in inner function')
        return function(name).title() # not changed yet
    return inner

def add_mr(function):
    def inner(name):
        print(name, 'line 92')
        name = f"Mr/Mrs {name}"
        return function(name)
    return inner        

# use a decorator/closure
def greet_some_humans(name):
    # API, Test driven development
    return "Good morning " + name    


greet_some_humans_with_decorator = make_title_in_word(greet_some_humans)
greet_some_humans_with_decorator = add_mr(greet_some_humans)

# greet_some_humans = add_mr(greet_some_humans)

# print(greet_some_humans_with_decorator('wojciech doe'))
# print(greet_some_humans('wojciech doe'))
# capitalize names

# end of the month
# Dependency injection
# Inversion of control
# @access_database
# @send_email_confirmation
# def charge_client(credit_card_number):
#     pass

# reminder on list comprehensions

# names = ['peter doe', 'peer doe', 'mary doe', 'tom doe', 'john doe']
# capital_names = []

# # for n in names:
# #     capital_names.append(n.capitalize())


# capital_names = [  n.title() for n in names ]
# # filter out all names that have `p` start with
# # filter() 
# no_ps = [n.title() for n in names if 'p' not in n]
# print(no_ps)


# processing unkown arguments
# def add_mr(function):
#     def inner(*args):
#     #     full_string = ''
#     #     for s in args: 
#     #         full_string += s + ' '
#         name = f"Mr/Mrs {' '.join([ n.title() for n in args])}"
#         return function(name)
#     return inner        

# @add_mr
# def greet_some_humans(name):
#     # API, Test driven development
#     return "Good morning " + name    

# print(greet_some_humans('peer', 'doe', 'johnson', 'MP', 'Felipe'))


add = lambda a, b: a + b

print(add(1, 2)) # 3

subtract = lambda c, d: c - d
print(subtract(15, 7))

@check_divisor
def div(e,f):
    return e / f

# division = lambda e, f: div(e,f)
# division(4,0)

database_of_names = { 'female': ['Shabanita'], 'male': ['Shabanino']}
# to a string, add Mr/Ms to a name
# add_string = lambda prefix, name, gender: f"{'Ms' if gender == 'female' else 'Mr'} {name}"

# add_string = lambda **kwargs: f"{'Ms' if kwargs['gender'] == 'female' else 'Mr'} {kwargs['name']}"

# def add_string(prefix, name):
#     return f"{prefix} {name}"
# print(add_string(name='Shaban', gender='male' ))


# print(division(9, 10))

# using lambdas within decorators

# def check_divisor(func):
#     # def inner(a, b):
#     #     if b == 0:
#     #         print("You cannot divide by 0")
#     #         return # stop here if there is 0. (Break in while loop?)
#     #     return func(a,b)
#     import pdb; pdb.set_trace()
#     return lambda a, b: "You cannot divide by 0" if b == 0 else func(a,b)


# @check_divisor
# def div(e,f):    
#     return e / f

def capitalize_name(func):
    inner = lambda name: func(name).title()
    return inner    

@capitalize_name
def greet(name):
    return name
print(greet('test'))

# support arguments with lambdas too

def capitalize_name(func):
    inner = lambda *args: func(*args).title()
    return inner    

@capitalize_name
def greet(*args):
    return ' '.join(args)

print(greet('test', 'two', 'Fausto'))    