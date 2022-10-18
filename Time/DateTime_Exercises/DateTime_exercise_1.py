######################################
####### DateTime - Basics 1 ##########
######################################

from datetime import datetime

current_datetime = datetime.now()

'''
print(dir(current_datetime))      # print the dir means The dir() function returns all properties and methods of the specified object, without the values. This function will return all the properties and methods, even built-in properties which are default for all object.
'''

# Task 1
print("\n###### Task 1 ######")

print(current_datetime.year)


# Task 2
print("\n###### Task 2 ######")

some_date = datetime(2021, 7, 14)

current_date = datetime.isoweekday(some_date)

print(current_date)

# Task 3
print("\n###### Task 3 ######\n")

year = int(input('Enter year : '))
 
if (year%4 == 0 and year%100 != 0) or (year%400 == 0) :
    print(year, "is a leap year.")
else :
    print(year, "is not a leap year.")

# Task 4
print("\n###### Task 4 ######\n")

date_as_string = "Feb 14 2021 8:30AM"

format_date = datetime.strptime(date_as_string, "%b %d %Y %I:%M%p")

print(format_date)