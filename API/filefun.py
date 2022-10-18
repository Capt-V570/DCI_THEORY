#######################################################
#### VIRTUAL ENVIRONMENT and API (14 October 2022) ####
#######################################################


f = open("book.txt")
# read the contents of the file
lines = f.readlines()
print(lines)

# Writing into a file:
f = open("book.txt", "a")   # 'a' stands for 'append'
# write something
f.write("Hello class\n")
# close the file descriptor 
f.close()

'''
# Test-case by adding 1 million numbers to a file:
f = open("book.txt", "a")   # 'a' stands for 'append'
for n in range(1000001): # add 1 million numbers to the file:
    f.write(f"{n}\n")
f.close()
'''
# APIs:
import requests
import pprint

r = requests.get('https://pokeapi.co/api/v2/pokemon/ditto')
print(r.json())

# or use Postman -it's better (more clear and clean)


'''
VICTOR's Theory Notes for this day
'''

# Topic summary
# Units for study
# - Input/Output
# - Basic tools and libraries

# Summary of the minimum knowledge you need
# ============================================

#  - Reading from a file in Python
#  https://www.w3schools.com/python/python_file_open.asp

# To read a file with the name book.txt we could write code like this:

#  f = open('book.txt')
 
# To view the contents of this file, we can write code like the one you see below and
# store it in a variable.

# lines = f.readlines()
# print(lines)
 
#  - Writing to a file in Python
#  https://www.w3schools.com/python/python_file_write.asp

# Writing to a file. This command open has several modes, we shall use the append mode to add 
# content to the file.

# f = open('book.txt', 'a')  
# #  write
#  f.write("Hello class")
# # (when we open a file, we close it, this is the same as saving the file
#  f.close()

# In class exercise
#  I would like you to write numbers from 1 to 1000,000
#  Solution
# f = open('book.txt', 'w')
# for i in range(1000000):
#     f.write(f"{i}\n")
# f.close()    

# Read, class book in Chapter 14. You can also visit the section in Rose 
# called Input/Output

# Refresher from Markus' class
# ==============================

# creating a virtual env
# ----------------------

# python3 -m venv venv
