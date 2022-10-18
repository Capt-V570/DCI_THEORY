######################################
####### DateTime - Basics 2 ##########
######################################

from datetime import datetime
from time import strftime

current_datetime = datetime.now()

print("\nPRECONDITION\nCurrent datetime is:", current_datetime)

# Task 1
print("\n###### Task 1 ######\n")

from datetime import timedelta          # importing timedelta module

two_weeks_prior = timedelta(days = 15)       # setting timedelta variable to 15 days

print(current_datetime - two_weeks_prior)    # subtracting the 15 days timedelta from current datetime and printing it

# Task 2
print("\n###### Task 2 ######\n")

week_ahead = timedelta(days = 7)        # setting timedelta to 7 days

print(current_datetime + week_ahead)    # adding the 7 days timedelta to current datetime and printing it

# Task 3
print("\n###### Task 3 ######\n")

start_date = datetime(year=2020, month=1, day=1)

payment_due = timedelta(days = 390)     # setting timedelta to 1 year and 25 days

rent_due = start_date + payment_due

format_rent_due = rent_due.strftime("%d %B, %Y")

print("Hello Friedrich, your rent of 300 € is due on", format_rent_due)




