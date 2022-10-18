###########################################
########### Reg_Ex EXPLAINATION ###########
###########################################




import re  # import the regular expression library

text_to_be_searched = "some text mail@web.de some text"  # target text

pattern = r"([type_here_the_reg-ex_pattern]])"      # the actual regular expression (r stands for raw string)

#x = re.search(pattern, text_to_be_searched)        # 1st method - using the pattern to search the target text
x = re.findall(pattern, text_to_be_searched)        # 2nd method - using the pattern to find all occurrencies within the target text

print(x)    # printing out the match

'''
EXERCISE 4 GROUPS:
Go to: https://regex101.com/

Search in Groups:
ALPHA - what does ^  and $ do?  + example
BRAVO - what does \w and + do?  + example
CHARLIE - what does (\w{3,3}) do? + example
DELTA - what does [a-z], [A-Z] and . do? + example
'''