

from sys import last_traceback


def greeting(first_name, last_name, salutation ="Dear Sir/Madam"):
    return f"{salutation} {first_name}, {last_name,}, you are invited to a gala evening!"

full_name = "Fausto Ferrara"
first_name = "Fausto"
last_name = "Ferrara"

# prone to errors !!! logical data entry errors
print(full_name('last name', 'first name'))
# very hard to make mistakes!
print(full_name(first_name='first name', last_name='last name'))
print(full_name(last_name='last name', first_name='first name'))