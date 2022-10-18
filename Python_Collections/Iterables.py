#######################
###### ITERABLES ######
#######################


'''Iterables are something your can loop over'''

# function ' any() ' & ' all() ':

# these 2 functions returns True or False wether 'any' or 'all' of the values contained in them are 'truthy', or not.


netflix_subscribers = [
    {"name": "Fausto", "paid": False},
    {"name": "Jacques", "paid": True},
    {"name": "Pasco", "paid": True},
    {"name": "Wessam", "paid": False},
    {"name": "Emily", "paid": False},
]

paid = []
for user in netflix_subscribers:
    if user['paid']:
        paid.append(user)
# logic @ boolean 
print(len(paid), len(netflix_subscribers))

have_all_paid = len(paid) == len(netflix_subscribers)

have_all_paid = all([user['paid'] for user in netflix_subscribers])


# map() -- function to map/reduce:
# Give you a list and your trasform the contents of that list (mutable iterable)

names = ["fausto", "mirjam", "peer", "pasco", "shaban"]


'''
# classic version (for loop):

all_names_capitalize = [] 

for name in names:
    all_names_capitalize.append(name.capitalize())
'''

# version with map(<function>, <iterable>)
all_names_capitalize = map(lambda name: name.capitalize(), names)
print(list(all_names_capitalize))


# alternative version with function:

def capitalize(name):
    return name.capitalize()



names = ["fausto doe", "mirjam doe", "peer doe", "pasco doe", "shaban doe"]

# import string:
all_names_capitalize = map(capitalize, names)
# shorter method:
all_names_capitalize = map(lambda name: name.title(), names)
#also:
all_names_capitalize = map(str.title, names)

# solving by creating a function (hard coded solution):
def custom(name):
    # list comprehensions
    split_name = name.split(' ')
    full_string = ''
    for n in split_name:
        full_string += n.capitalize() + " "
    return full_string

all_names_capitalize = map(custom, names)

print(list(all_names_capitalize))

# extra credit
# names = [{'name': 'jacque doe'}, {'name': 'peer doe'}, {'name': 'mirjam doe'}, {'name': 'shaban doe'}] 


######## FILTER #######

names = ["reiner", "mirjam", "peer"]

# filter out banes that end with er # - classical/traditional
for name in names.copy():
    if name.endswith("er"):
        names.remove(name)

print(names)

# version with filter():

names = filter(lambda name: not name.endswith("er"), names)
print(list(names))


names = [{'name': 'jacque doe'}, {'name': 'peer doe'}, {'name': 'mirjam doe'}, {'name': 'shaban doe'}]

# hard coded version (=creating and using a function):
def filtering_jacque(name_dictionary):
    if name_dictionary["name"].startswith("jacque"):
        return False
    return True

names = filter(filtering_jacque, names)


# alternative version using 'lambda function':

names = filter(lambda name_dictionary: not name_dictionary['name'].startswith('jacque'), names)
print(list(names))

