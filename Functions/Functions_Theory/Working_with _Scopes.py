############################################
####### SCOPES (Working with Scopes) #######
############################################

'''
we are going to explain SCOPES by changing names within a function
'''

from types import new_class


first_name = ""     # global variable
last_name = "Doe"

def full_name():
    first_name = "Fausto"   # local variable (with local scope)
    last_name = "Ferrara"
    #print(first_name, "-> first name")     # however, we usually don't use to print sth within a function
    #print(last_name, "-> last name")       # however, we usually don't use to print sth within a function
    return f"{first_name} {last_name}"

# what is the value of first_name ?

print(full_name())
print(first_name)
print(last_name)




first_name = "Michel"     # global variable
last_name = "Doe"


def full_name():
    # first_name = "Fausto"   # local variable (with local scope)
    last_name = "Ferrara"
    print(first_name, last_name) 
    
    def add_sir(name):
        return f"Sir {name} {last_name}"

    new_full_name = add_sir(first_name)
    return new_full_name