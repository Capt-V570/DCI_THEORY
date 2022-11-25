# Popular convention by ORM developers
# Singular form of a class name to represent a table
# table will be mostly plural
import psycopg2

connection = psycopg2.connect(
    user="postgres",
    password="postgres",
    host="localhost",
    port="5432",
    database="flask_intro",
)

cur = connection.cursor()


class Reminder:
    # constructor:
    def __init__(self, title, description) -> None:
        self.title = title
        self.description = description

    def save(self):
        """Stores the value of title and description in the table"""
        cur.execute(
            f"""INSERT INTO reminders (title, description)
            VALUES('{self.title}', '{self.description}') RETURNING id, title, description"""
        )
        connection.commit()

        values = cur.fetchone()
        print(values)

    # return the instance
