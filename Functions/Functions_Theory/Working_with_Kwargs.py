############################################
####### KWARGS (Keywords arguments) ########
############################################

'''
we are going to explain KWARGS by instroducing Dictionaries
'''
# *args! (**kwargs)
# data structure -- called a dictionary

# Explaination of 'Dictionary':
# Example: Dictonary English to German
#                    Good day - Guten Tag

greetings = {
    "key": "value",
    "table": "a place to put your food on",
    "car": "a maschine to help humans to move from point A to point B"
}

#def hello(first_name, last_name="Doe")

'''
NOTE:
def FUNCTION(ARGS 1st!!!, KWARGS 2nd!!!)
'''

def full_name(*args, **kwargs):        # kwargs are DICTIONARIES
    print("--kwargs: ->", kwargs)
    print("---args: ->", args)
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    return f"{args[0]} {first_name} {last_name}"

# how to use it :

print(full_name("Good morning", first_name = "Sharlene", last_name = "Doe", location = "Berlin"))

# how to get data from people:
print(full_name(first_name=input("Hello", "What is your first name? ", last_name="Doe")))

