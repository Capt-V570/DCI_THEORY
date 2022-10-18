# Create two applications in two files. Each of these is to parse arguments given on the command line.
# 
# This App_1 is to be used with sys.argv: arguments at the command line interface (CLI) 
#       - sys.argv is a list
#       - sys.argv is always available
#       - sys.argv will always have at least one item (a string with a program name)
#       - any arguments passed at the command line will also be added to the sys.argv list
#       - we can check to see if any arguments have been passed, by checking the len() of sys.argv

import sys          # importing sys library for using arguments at the command line interface (CLI)

'''
# number of Arguments in this program
if len(sys.argv) != 3:
    exit("Please pass 2 arguments only")
'''

default_mode = sys.argv[1]      # "slow mode enabled (normal operating mode)"
fast_mode = sys.argv[2]         # "fast mode enabled"

# print(sys.argv) - at this stage the system will receive only 2 arguments

help = """\n [HELP] For further guidance on mode operation see as follow:
                --help : return the help options
                --fast : enable the fast mode of the program
                --v    : show verbose information of the program
                """
verbose = """\n [VERBOSE HELP]  The operation of this program is essentially 
                via means of operability between default 'SLOW MODE' and 'FAST MODE'.
                At this stage of development there aren't any other commands, 
                to be used due to the fact that the programmer who did this 'masterpiece', 
                had too little amount of knowlege and time, before creating this program.

                Now, one of the following two statements is true:
                    - either the programmer will spend every single night studying REAL hard 'sys.argv';
                    - or, the programmer will receive a lot of detailed inputs from better 'user_story'.
                
                If you still wish to run arguments from CLI for this program, 
                which is programmed with 'sys.argv', please use one of the following commands:

                    --help : to obtain help
                    --fast : to engage FAST MODE
                    --v    : to expose a very verbose detail of how to use this program.

                    NOTE: if no 'FAST MODE' is enabled, the system will actually run in the default 
                    oprational mode, which is the 'SLOW MODE'


                End of (verbose) Story, Morning Glory.
                """

# creating a 'for' loop for conditional statements:

fast_mode = False 

for i in sys.argv[1:]:
    if i == "--help":
        print(help)
    elif i == "--fast":
        fast_mode = True
        print("\n[LET'S ROCK IT!!!] FAST MODE ENABLED\n")
    elif i == "--v":
        print(verbose)
    else:
        exit("\n[NOTE] For this Program, please pass 2 Valid Arguments only\n")
        
for i in sys.argv[2]:
    if i != "--fast":
        fast_mode = False
        print("\n[ATTENTION!!!] Default Operational Mode Auto-Engaged: SLOW MODE ENABLED\n")
    elif i == None:
        fast_mode = False
        exit("\n[ATTENTION!!!] Default Operational Mode Auto-Engaged: SLOW MODE ENABLED\n")



'''
fast_mode = True 

for i in sys.argv[:2]:
    if i == "--help":
        print(help)
    elif i == "--fast":
        print("\nFAST MODE ENABLED\n")
    elif i == "--v":
        print(verbose)
    else:
        fast_mode = False
        print("Default Operational Mode Automatically Engaged: SLOW MODE ENABLED")



fast_mode = True

for i in sys.argv[:2]:
    if i == "--help":
        print(help)
    elif i == "--fast":
        print("FAST MODE ON")
    else:
        print("NORMAL MODE IS NOW AUTOMATICALLY ENGAGED")
'''

