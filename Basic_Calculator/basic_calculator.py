# Task 1 - create a simply calculator

'''
# create a basic calculator 
numerator = float(input("Please enter a number to divide (aka 'numerator'): "))
denominator = float(input("Please enter the 'denominator': "))

result = numerator / denominator
format_result = "{:.2f}".format(result)

print(format_result)
'''

# Task 2 - now use the "sys.argv" to use the calculator via shell with arguments

# STEP 1 - import sys library
import sys

# STEP 2 - re-do the calculator using arguments
num1 = float(sys.argv[1])
num2 = float(sys.argv[2])

result = (float(num1) / float(num2))
format_result = "{:.2f}".format(result)

if num2 == 0:
    print("This operation is not possible")
elif num2 != 0:
    print(format_result) # comment something here
else:
    print(format_result)
