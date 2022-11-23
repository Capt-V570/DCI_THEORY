"""static methods, classmethods and instance method"""


# pseudo-code -> turn into real code:
import psycopg2

# functions (to connect to the database)


# functions (to connect to the database)
def get_connection():
    connection = psycopg2.connect("dbname=november user=postgres")
    cur = connection.cursor()
    return connection, cur


# IF the code above is denied permission, use this code instead:
# def get_connection():
#     conn = psycopg2.connect(
#         database="november",
#         user = "postgres",
#         host = "5432",
#         password = "postgres")
#     cur = conn.cursor()
#     return (conn, cur) # Tuple


def write_to_db(connection):
    connection.commit()


class Human:
    # first name, last name
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    # walking(), eating(), greeting(), save()

    """
    fausto = Human('fausto', 'doe')
    fausto.save()
    """

    def save(self):
        # TODO: change this, make updates to re-assignment:
        connection, cur = get_connection()
        # name -> first name and last name together:
        name = f"{self.first_name} {self.last_name}"
        cur.execute(f"INSERT INTO users(name) VALUES('{name}')")
        write_to_db(connection)

    # ORM -> Object Relation Mappers
    # Classes -> tables (methods represent SQL actions)
    @staticmethod
    def delete(id):
        breakpoint()
        print("Deleting human with id", id)

    # Human.delete(1) # stati method

    # repper:
    def __repr__(self) -> str:
        return f"first_name={self.first_name}, last_name={self.last_name}"

    @classmethod
    def get(cls, id):
        print("Getting a human")
        connection, cur = get_connection()
        cur.execute(f"SELECT name FROM users WHERE id={id}")
        h = cur.fetchone()
        name = h[0]
        f_name, l_name = name.split(" ")
        print(f_name, l_name)
        human_instance = cls(f_name, l_name)
        return human_instance


if __name__ == "__main__":
    # Human.delete(1)
    x = Human.get(1)
    print(x)
    # h = Human("X", "Y")
    # h.save()

    # # Human.delete(1) # static method
    # h.delete(1) # instance method

    h = Human("John", "English")
    h.save()
    h = Human("Victor", "Aubemayang")
    h.save()
    h = Human("Fausto", "Doe")
    h.save()
