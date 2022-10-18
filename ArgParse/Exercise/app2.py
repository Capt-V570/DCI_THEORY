# Create two applications in two files. Each of these is to parse arguments given on the command line.
# 
# This App_2 is to be used with 'ArgPars': arguments at the command line interface (CLI) 
# Using 'argparse' module is a better option than the above two options as it provides a lot 
# of options such as positional arguments, default value for arguments, help message, 
# specifying data type of argument etc. 
# Note: As a default optional argument, it includes -h, along with its long version –help.

import argparse         # importing library to use 'ArgParse' arguments
import sys              # import sys.argv lib to use 'Sys.Argv' from CLI
import time             # import time lib to play with time while printing

speed = float(1.5)
time.sleep(speed)

parser = argparse.ArgumentParser(Description = "Add Name, Surname and Age to the Invitation List")     # initialize parser & giving it a description name
parser.add_argument("-n", "--name",     type=str, help="Name of the Person")            # adding argument for the Name of person
parser.add_argument("-s", "--surname",  type=str, help="Last name of the Person")       # adding argument for the Surname of person
parser.add_argument("-a", "--age",      type=int, help="Age of the Person")             # adding argument for the Age of the person
parser.add_argument("-f", "--fast",     type=str, help="Fast Mode Enabled")             # adding argument for Enabling the Fast Mode
parser.add_argument("-h", "--help",     type=str, help="Calling for Help")              # adding argument for Calling for Help

args = parser.parse_args()      # create 'args' object and getting parser object info. Read Arguments from 'Command Line Interface'

fast_mode = sys.argv[4]

if args.fast == None:
    print("Slow Mode Engaged")

if args.f == None:
    args.f = "Larry"

if args.l == None:
    args.l = "Hanson"

if args.a == None:
    args.a = 100

time.sleep


'''
# creating the function 
def list():
    first_name  = sys.argv[1]
    last_name   = sys.argv[2]
    age         = sys.argv[3]
    return f{first_name}{last_name}{age}
'''
