



class Person:
    # dunder methods --> double underscore methods
    # 'self' means the "entity" -> 'self' refers to the instance of the class
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def greeting(self):
        return f"Good morning, my name is {self.name}"



# "function"
a = Person("Peer")
#print(a)
print(a.greeting())
b = Person("Shaban")
c = Person("Fausto")
d = Person("Emily")
f = Person("Victor")
e = Person("Maria")
# dot notation
# print(a.name)
# print(b.name)

