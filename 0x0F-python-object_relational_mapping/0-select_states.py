#!/usr/bin/python3
"""
Module that lists all states from mySQL database
"""
import sys
import MySQLdb


def list_states(username, password, database):
    """
    lists all states from db: hbtn_0e_0_usa

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
    query = "SELECT * FROM states ORDER BY id ASC"
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
    list_states(username, password, database)
