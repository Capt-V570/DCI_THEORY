############################################
####### KWARGS (Keywords arguments) ########
############################################

'''
# EXERCISE: Using the list below: can you change the function to use it as a dictionary?

last_name = ["Doe"]
# "Pass by reference" variables can change
def full_name(last_name):
    # variations 
    last_name[0] = "Ferrara"
    return last_name

full_name(last_name)
print(last_name)

# >> RECAP: <<

# *args! (**kwargs)
# data structure -- called a dictionary

# Explaination of 'Dictionary':
# Example: Dictonary English to German
#                    Good day - Guten Tag

dictiornary = {
    "key": "value",
    "table": "a place to put your food on",
    "car": "a maschine to help humans to move from point A to point B"
}


NOTE:
def FUNCTION(ARGS 1st!!!, KWARGS 2nd!!!)


def full_name(*args, **kwargs):        # kwargs are DICTIONARIES
    print("--kwargs: ->", kwargs)
    print("---args: ->", args)
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f"{args[0]} {first_name} {last_name}"

'''

print("\n >>> EXERCISE 1 - version 1 <<<\n")

# list dictionary: 
full_name = {"first_name": "Fausto", "last_name": "Doe"}        # global variable

# "Pass by reference" variables can change
def name(full_name):                                            # local variable
    # variations be like:
    #full_name["first_name"] = "Michel"
    full_name["last_name"] = "Ferrara"
    def salutation():
        salute = f"Capt. {full_name['first_name']} {full_name['last_name']}\n"
        return salute
    return salutation()

print(name(full_name))


print("\n >>> EXERCISE 1 - version 2 <<<\n")

# list dictionary: 
full_name = {"first_name": "Fausto", "last_name": "Doe"}        # global variable

# "Pass by reference" variables can change
def name(full_name):                                            # local variable
    # variations be like:
    #full_name["first_name"] = "Michel"
    full_name["last_name"] = "Ferrara"
    return f"Capt. {full_name['first_name']} {full_name['last_name']}"

print(name(full_name))


print("\n >>> EXERCISE 1 - version 3 <<<\n")

# list dictionary: 
global_variable = {"first_name": "Fausto", "last_name": "Doe"}        # global variable

# "Pass by reference" variables can change
def function_to_change():                                            # local variable
    global_variable["first_name"] = "Michel"
    global_variable.update({"last_name": "Ferrara"})
    print(global_variable)
    return global_variable

print(function_to_change())
