import pymysql

def create_mysql_connection():
    """
    This function creates a MySQL database connection.

    Returns:
        The connection to the MySQL database.
    """
    connection = pymysql.connect(
        host='localhost',
        user='username',
        password='password',
        database='mydatabase'
    )
    return connection

def insert_planet(connection, name, radius, mass):
    """
    This function inserts a planet into the MySQL database.

    Args:
        connection: The connection to the MySQL database.
        name: The name of the planet.
        radius: The radius of the planet.
        mass: The mass of the planet.

    Returns:
        None.
    """
    cursor = connection.cursor()
    sql = "INSERT INTO planets (name, radius, mass) VALUES (%s, %s, %s)"
    values = (name, radius, mass)
    cursor.execute(sql, values)
    connection.commit()

if __name__ == "__main__":
    connection = create_mysql_connection()

    insert_planet(connection, "Earth", 6371, 5.972e24)
    insert_planet(connection, "Mars", 3389, 6.421e23)
    insert_planet(connection, "Jupiter", 69911, 1.898e27)

    connection.close()
