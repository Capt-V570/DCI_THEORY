#################################################################
###### FUNCTIONS explained with some basic Math operations ######
#################################################################

'''
# take 2 random variables:

x = 3
y = 4

# let's add the two numbers:

z = x + y 
print(z)
'''

# Now, let's make it sustainable! (meaning: let's use the same variable numbers for different types of operations) such as for:
# - addition
# - subtraction
# - moltiplication
# - division


def sum(num1, num2):                # local variables
    return num1 + num2

def subtraction(num1, num2):        # local variables
    return num1 - num2

def moltiplication(num1, num2):     # local variables
    return num1 * num2

def division(num1, num2):           # local variables
    if num2 == 0:   # exeption in case the second operand is '0'
        print("You cannot divide a number by zero")
        return      # simply writing 'return' will allow the code not to break (like usually would happens in this case of a division by 0)
    else:
        return num1 / num2

'''
# call the "global variables"
x = 3
y = 4

# "placeholder" -- we replace with actual "values"/variable
print(sum(x,y))

# NOTE: 'return' statements of a function -- do not -- show on the terminal CLI (Command Line interface), unless you 'print'!!)

'''

# provided following 'global' variables

x = 3
y = 4

# in case of an addition with these 2 numbers, we will now use:
print("\nADDITION:\n")
print(sum(x, y))

# in case of a subtraction between these 2 numbers, we will now use:
print("\nSUBTRACTION:\n")
print(subtraction(x, y))

# in case of a moltiplication between these 2 numbers, we will now use:
print("\nMOLTIPLICATION:\n")
print(moltiplication(x, y))

# in case of a division between these 2 numbers, we will now use:
print("\nDIVISION:\n")
print(division(x, y))