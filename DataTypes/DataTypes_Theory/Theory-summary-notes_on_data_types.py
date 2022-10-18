# """

# As of today, which "primitive" data types have we seen?

# - string 
# - integer
# - Float 
# - Boolean

# Compound data types
# ------ 
# - Lists
# - Tuples

# """

# # What is a tuple?

# # an ordered sequence of elements, can mix element types of data

# # name = ('Mirjam', 'Lingoda')
# # other_name = ('Peer', 'Hofman')

# # # tuples (are immutable)

# # name = name + other_name
# # # print(name)

# # numbers = (1,2,3,4,5,6,7,8,9)
# # print(numbers[0:1]) # 2, 3, 4, 5

# # # inbuilt "len" function/method
# # print(len(numbers))
# # print(numbers[0])

# # # negative indexing
# # print(numbers[-2])


# # quotient and remainder
# # 4 / 2 = 2; 5 / 3 --> 1 (remainder: 2)
# # I want to return both the quotient and remainder

# from re import X


# def quotient_remainder(x, y):
#     quotient = x // y # integer division (floor)
#     remainder = x % y # modulo operation
#     return (quotient, remainder)

# # assignment
# (q, r) = quotient_remainder(5, 3) # unpack a tuple


# x = 45
# y = 50

# # can you swap the values?
# # print(f"x->{x}, y=> {y}")
# # temporary_store = x
# # x = y
# # y = temporary_store
# # print(f"x->{x}, y=> {y}")

# # swap in python
# (x, y) = (y, x)
# # print(f"x->{x}, y=> {y}")

# # print(q)
# # print(r)

# """
# Design a function that takes in a gender and a firstname and last name
# If the gender is "male", return a greeting (Good morning Mr. <first name>) and a fullname
# If the gender is "female", return a greeting (Good morning Ms. <first name>) and a 
# """

# def greeting_fullname(first_name, last_name, gender="Mr./Ms."):
#     full_name = f'{first_name} {last_name}'
#     greeting = ''
#     if gender == 'male':
#         greeting = f"Good morning Mr. {first_name}"
#     elif gender == 'female':
#         greeting = f"Good morning Ms. {first_name}"
#     else:
#         greeting = f"Good morning {gender} {first_name}"
#     return (greeting, full_name)




# # test case
# # print(greeting_fullname('Alexander', 'Simakov', 'male')) # --> (Good morning Mr. Alexander, 'Alexander Simakov')
# # print(greeting_fullname('Alexandra', 'Simakovina', 'female')) # --> (Good morning Mr. Alexander, 'Alexander Simakov')
# # print(greeting_fullname('Alexandra', 'Simakovina'))


# # Iteration? Going through each element of a collection 
# # sizes = ('S', 'L', 'XL', '4th' )
# # # for loops? - slices?
# # for s in sizes:
# #     print(s) # 99% 
# # print(sizes[0])


# # What is a list?
# # Ordered sequence of information that are accessible by an index
# # we denote by the use of square brackets->  [ ]
# # list contain elements that can be mixed data types (not common/not encouraged) and pure or homogenous data types
# # "m" word?? Lists are mutable!! (Changeable)


# # sizes = ['l','m', 'xl', 'xxl']
# # print(len(sizes))
# # access items in a list
# # print(sizes[0])

# # i = 100
# # print(sizes[i - 99]) # expressions!! 

# # sizes[0] = 'L'
# # sizes.insert(1, 'S')
# # print(sizes)

# # for loop iteration

# # design a while loop?

# # sizes = ['l','m', 'xl', 'xxl']

# # s = 0 # counter variable
# # # > , < , <=, >=
# # while s < len(sizes): # 99.9% WHILE [CONDITION -has to be true]:
# #     print(sizes[s])
# #     s += 1

# # for s in sizes:
# #     print(s)

# # Exercise

# # To get a total, we have a function that looks like this, rewrite (refactor) the function to use a while loop

# def total_list(lst):
#     total = 0
#     # counter variable 
#     index = 0
#     while index < len(lst):
#         total += lst[index]
#         index += 1
#     return total
# # test case
# print(total_list([1, 2, 3]))   # answer is 6
# print(total_list([3, 3, 3]))   # answer is 6




# def t_while(lst):
#     total = 0
#     index = 0
#     while index < len(lst):
#         total += lst[index]
#         index += 1
#     return total

# # print(t_while([1,2,3]))

# # TODO: Talk about while loop again! Talk about for loop again!


# weight = ['10kg', '20kg', '30kg']

# # print(f"You are {weight[0]}")
# # print(f"You are {weight[1]}")
# # print(f"You are {weight[2]}")
# # normal "for" loop
# # for w in weight: 
# #     print(f"You are {w}")

# # while loop: print the following word: "You are 10kg"
# counter = 0
# weight = ['10kg', '20kg', '30kg']
# while counter < len(weight): # 99% # false !    
#     # print(weight[counter])
#     counter += 1
    
    
    # we have to change the value of the counter
    
    # accessing items from a list or tuple, index notation
    # LIST[INDEX] -> weight[w]
    # print(f"You are {weight[w]}") # 99.9% 
    # w += 1




# colors = ['red', 'green', 'yellow']    

# string = ""
# for e in colors:
#     # string concatenation 
#     string += e
# print(string)    
# "redgreenyellow"


# Operations on lists
# add things to list

lst = []
lst.append(5)
# print(lst)

list_a = [1,2,3]
list_b = [4, 5, 6]
lst_3 = list_a + list_b # list_a remains the same, list_b remains the same
# print(lst_3)

# we can mutate a list
list_a.extend(list_b)
# list_b remains the same, list_a now has new values
print(list_a)

# deleting a index
# del list_a[5]
# print(list_a)

# list_a.pop() # removes the last item and returns the removed item
# print(list_a)

# list_a.remove(3) # This one does not need an index
# print(list_a)

# duplicates = [1,2,2,2,2,2,2,3,3]
# # if duplicates == 2? 
# duplicates.remove(2)
# print(duplicates)
