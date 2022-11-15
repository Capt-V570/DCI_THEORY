from flask import Flask, jsonify, request

app = Flask(__name__)

# methods that represent URLs or links

# Home or Root route!
REMINDERS = []


@app.route("/")
def index():
    # JSON ->
    return jsonify()


# we want to store "reminders"

# how do we save reminders?


@app.route("/add-reminder", methods=["POST"])
def add_reminder():
    print("@@@@@@@@")
    print(request.json)
    REMINDERS.append(request.json)
    print("@@@@@@@@")
    # Exercise, add the reminders (dictionaries) to the REMINDERS constant
    return jsonify({"reminders": REMINDERS})


# Core HTTP verbs a developer must know
# - GET
# - POST
# - DELETE
# - PATCH


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5050)
