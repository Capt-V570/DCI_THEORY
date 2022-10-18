# REGULAR EXPRESSION

# Difference between 're.search' and 're.match'

# Python offers two different primitive operations based on regular expressions: 
#       - 'match' checks for a match only at the beginning of the string, while;
#       - 'search' checks for a match anywhere in the string. 

# Both of these 2 methods return the span of the word/text searched. 
# The difference between the se 2 methods is that if the word/text searched 
# is NOT at the beginning of the string, then 'match' will simply return 'None'.

# The reason to use 'match' are: 
#       - the speed: due to the fact that 'match' is faster than 'search' for returning 
#                   the indexing span of the word or text that you wanna search.
#       - for text validation, to check if the first item of a text corrisponds to the 


'Play with both option to check differences between these 2 methods'

import re           # import Regular Expression module (library)
 
Substring = "string"
 
 
String1 ='''We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''
String2 ='''string We are learning regex with geeksforgeeks
         regex is very useful for string matching.
          It is fast too.'''
 
# Use of re.search() Method
print(re.search(Substring, String1, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String1, re.IGNORECASE))
 
# Use of re.search() Method
print(re.search(Substring, String2, re.IGNORECASE))
# Use of re.match() Method
print(re.match(Substring, String2, re.IGNORECASE))


