"""
Concepts:

- function
- decorator
- list
- dictionary
- library (flask, psycopg2) - imported and instantiated a class

HTTP Verbs - action word, doing word - "to be", "tun", "fare", "me bo",

- GET (take something from somewhere or someone, fetching something)

- POST (sent letters? shipped something, put in a specific place)

- DELETE (remove something, get rid of something)

- PATCH (repair, update just a small part of something)

- PUT (change everything)
"""

# list_of_users = [
#     {"name": "Wojciech", "location": "Berlin"},
#     {"name": "Waheed", "location": "Frankfurt"},
# ]

# # find index?
# index = None
# for i, item in enumerate(list_of_users):
#     if item['name'] == 'Wojciech':
#         index = i

# if index:
#     # 3 ways
#     list_of_users.pop(index)

# change the name?
# dictionary["name"] = "Wojciech Sr."
# dictionary["location"] = "Munich"

# v1
# dictionary = { }

# v2
# dictionary.update({"name": "Wojciech Sr", "location": "Munich"})

# using a library
from flask import Flask, jsonify, request
import psycopg2

# instantiating a class (Flask)
app = Flask(__name__)

# List (empty)
REMINDERS = []

# Decorator
@app.route("/")
# Function
def index():
    # JSON ->
    return jsonify({"name": "Nadia"})
    # return jsonify("hello am a string")
    # return jsonify([{"name": "Shaban"}, {"name": "Fausto"}, (1,2,3)])


# we want to store "reminders"
#
# how do we save the reminders?


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    # Exercise, add the reminders (dictionaries) to the REMINDERS constant
    # write code here
    REMINDERS.append(request.json)
    # change the return value from empty list to have REMINDERS instead
    return jsonify({"reminders": REMINDERS})


# Core HTTP verbs a developer must know
# - GET
# - POST
# - DELETE
# - PATCH

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)
