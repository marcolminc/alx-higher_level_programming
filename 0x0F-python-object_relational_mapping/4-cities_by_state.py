#!/usr/bin/python3
"""
Module that lists all cities from the database hbtn_04_4_usa
"""
import sys
import MySQLdb


def list_cities(username, password, database):
    """
    lists all cities from the database hbtn_0e_4_usa

    Args:
        username: mysql username
        password: mysql password
        database: mysql database
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
            SELECT c.id, c.name, s.name
            FROM cities c
            JOIN states s ON c.state_id = s.id
            ORDER BY c.id
        """
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()


# usage:
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_cities(username, password, database)
