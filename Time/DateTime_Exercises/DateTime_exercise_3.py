######################################
####### DateTime - Basics 3 ##########
######################################

from datetime import datetime
from time import strftime

current_datetime = datetime.now()

print("\nPRECONDITION:\nCurrent datetime is:", current_datetime)

# Task 1
print("\n###### Task 1 ######\n")

b_day_input = datetime.fromisoformat(input("Enter your birthday in YYYY-MM-DD format: "))       # ask user to input the date of birth in ISO format

age = current_datetime - b_day_input                                # subtract current datetime from birthday date

print("\n Your age in days, hrs, minutes, seconds and millisenconds is:", age)     # print your age in days, hrs and secs + decimals

formatted_age = age

print("\n Your age in days, hrs, minutes, seconds and millisenconds is:", age)