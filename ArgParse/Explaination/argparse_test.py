# 'ArgParse' is short for Argument Parsing (or Argument 'sorting')
# [DEFINITION] An Argument is a value that is passed to a function when it is called. 
# It might be a variable, value or object which is passed to a function (or method) as input-.
# Arguments are written when we are calling the function. 
# TO RECAP:
# With Arguments we add additional information to a function of a program;
# this means that with Arguments we give specific inputs.
# In command line interface (CLI), Arguments are divided by empy spaces (e.g. git '--help' '-m')
# These spaces identify then the position of the arguments in the code.
# As matter of fact, every Argument we add to our python program, via 'CLI' is then embedded into a list, 
# callable with the option len(sys.argv)



import argparse     # import 'argparse' library to Parse the Arguments for calculating the Volume of a Cylinder
import math         # import math library 

# create the parser
parser = argparse.ArgumentParser(Description = "Calculate the volume of a Cylinder")    # initialize parser and giving it a description name
parser.add_argument("-r", "--radius", type=int, help="Radius of the Cylinder")          # adding argument for the Radius (of the Cylinder)
parser.add_argument("-H", "--height", type=int, help="Height of the Cylinder")          # adding argument for the Height (of the Cylinder)
args = parser.parse_args()      # create 'args' object and getting parser object info


# Creating the function to calculate the volume of the cylinder
def cylinder_volume(radius, height):
    vol = (math.pi) * (radius ** 2) * (height)
    return vol