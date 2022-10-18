################## EXERCISE 12 ####################

# RegEx Exercise

from ast import Index
import re       # import RegEx library

# Task 1

print("\n###### TASK 1 ######\n")

text1 = "Berlin is a world city of culture, politics, media and science."

pattern1 = r"(\s)"

solution1 = re.search(pattern1, text1)

print("The first white-space character is located at position:", solution1)

# Task 2

print("\n###### TASK 2 ######\n")

text2 = """Berlin is surrounded by the State of Brandenburg 
            and contiguous with Potsdam, Brandenburg's capital.""" 

pattern2 = r"^Frankfurt"

solution2 = re.search(pattern2, text2)

print(solution2)

# Tast 3

print("\n###### TASK 3 ######\n")

text3 = "Berlin is a city of culture."

pattern3 = r"(\s)"

solution3 = re.sub(pattern3, text3)

print(solution3)

