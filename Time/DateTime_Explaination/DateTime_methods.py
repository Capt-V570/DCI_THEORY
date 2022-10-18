from datetime import datetime

date_1 = "January 1, 2005"
date_2 = "2007, 1 January"

# Main type of 'datetime' are are follow:

# %B = Full month
# %d = numerical date
# %Y = Full year

# for a full list please see following link: https://www.geeksforgeeks.org/python-datetime-strptime-function/


converted_date_1 = datetime.strptime(date_1, "%B %d, %Y")           # it will result as: 2005-01-01 00:00:00
converted_date_2 = datetime.strptime(date_2, "%Y, %d %B")           # it will result as: 2007-01-01 00:00:00

print(converted_date_1)
print(converted_date_2)

# changing the formatting of the topic: 

# useful for cherrypicking [TBC]
