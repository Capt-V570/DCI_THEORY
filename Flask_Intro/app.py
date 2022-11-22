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

connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",  # database
    database="flask_intro",
)

cur = connection.cursor()

# instantiating a class (Flask)
app = Flask(__name__)

# List (empty)
REMINDERS = []

# Decorator
@app.route("/")
# Function
def index():
    # Fetch all the reminders from the database
    cur.execute("SELECT * FROM reminders;")

    # store in a variable
    reminder_data = cur.fetchall()  # get a list of TUPLES !
    # reminder_data = [{"title": item[0], "description": item[1]} for item in reminder_data ] # list comprehension
    print(reminder_data)

    columns = ["title", "description"]
    list_of_dictonary = []
    for item_in_tuple in reminder_data:
        temp_dict = {}
        # for index, value in enumerate(columns):
        #     temp_dict[columns[index]] = item_in_tuple[index]

        temp_dict["title"] = item_in_tuple[0]  # Mirjam ...
        temp_dict["description"] = item_in_tuple[1]  # She is ...

        list_of_dictonary.append(temp_dict)

    # JSON ->
    return jsonify({"reminders": list_of_dictonary})
    # return jsonify("hello am a string")
    # return jsonify([{"name": "Shaban"}, {"name": "Fausto"}, (1,2,3)])


"""
    # TODO: Exercise for the day (Submit on Tuesday):
    # Without using `pyscop2.extras.DictCursor`, make changes to the output
    # to return the following - a list of dictionaries
    # Instead of {
    "reminders": [
        [
            "Mirjam is awesome",
            "She is learning to code"
        ],
        [
            "Eat",
            "Food is healthy"
        ],
        [
            "Exercise",
            "Get your heart moving"
        ]
        ]
    }

    Return the following:
    }
    "reminders": [
        {
            "title": "Mirjam is awesome",
            "description": "She is learning to code"
        },
        {
            "title": "Eat",
            "description": "Food is healthy"
        },
        {
            "title": "Exercise",
            "description": "Get your heart moving"
        }
    ]
    }
"""


# we want to store "reminders"
#
# GET
# POST
# DELETE
# PATCH
# PUT
# how do we save the reminders?

# Decorator -- URL path call add-reminder
@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    try:
        title = request.json["title"]
    except KeyError:
        title = None

    # handle the exception (error handling)
    try:
        description = request.json["description"]
    except KeyError:
        description = None
    # Null
    print(f"INSERT INTO reminders (title, description) VALUES({title}, {description});")
    cur.execute(
        f"INSERT INTO reminders (title, description) VALUES('{title}', '{description}');"
    )
    connection.commit()
    print(title, description)
    # change the return value from empty list to have REMINDERS instead
    return jsonify({"reminders": REMINDERS})


@app.route("/reminders/<int:id>")
def reminder(id):
    cur.execute(f"SELECT * FROM reminders WHERE id = {id};")
    reminder_data = cur.fetchone()
    try:
        reminder_dict = {
            "id": id,
            "title": reminder_data[0],
            "description": reminder_data[1],
        }
        return jsonify(reminder_dict)
    except:
        return jsonify({"message": "Sorry something bad happened"}), 500


# DELETE
@app.route("/reminders/<int:id>", methods=["DELETE"])
def delete_reminder(id):
    # TODO: Write a query that deletes a reminder
    cur.execute(f"DELETE FROM reminders WHERE id={id};")
    # commit the changes
    connection.commit()
    return jsonify({"message": "Successfully deleted!"})


# what if we have 1000+ connections?
# Garbage colletion (memory management)
@app.route("/reminders/<int:id>/update", methods=["PUT"])
def update_reminder(id):
    cur.execute(
        f"""
        UPDATE reminders
        SET title='{request.json.get('title')}',
        description='{request.json.get('description')}'
        WHERE id={id}
    """
    )
    connection.commit()
    # Exercise: Return the updated information as a dictionary
    return jsonify({})


# Core HTTP verbs a developer must know
# - GET
# - POST
# - DELETE
# - PUT
# - PATCH

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)  # port for flask
