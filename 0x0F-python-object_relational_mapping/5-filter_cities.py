#!/usr/bin/python3
"""
Module that lists all cities of a state
"""
import sys
import MySQLdb


def list_cities(username, password, database, state):
    """
    lists all cities from the database hbtn_0e_4_usa

    Args:
        username: mysql username
        password: mysql password
        database: mysql database
        state: the state whose cities are filtered
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    cursor = db.cursor()
    query = """
                SELECT c.name
                FROM cities c
                JOIN states s ON c.state_id = s.id
                WHERE s.name = %s
                ORDER BY c.id ASC
            """
    cursor.execute(query, (state,))
    rows = cursor.fetchall()

    cities = [row[0] for row in rows]
    print(", ".join(cities))
    db.close()


# usage:
if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage:\
        {} <username> <password> <database> <state>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_cities(username, password, database, sys.argv[4])
