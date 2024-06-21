#!/usr/bin/python3
"""
Module that lists state(s) where name matches the passed argument
"""
import sys
import MySQLdb


def list_states(username, password, database, state):
    """
    lists state(s) where name is the passed argument for state

    Args:
        username: mysql username
        password: mysql password
        database: mysql database
        state: name of state
    """
    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY `name` = '{}' ".format(state)
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    db.close()


# usage:
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database, sys.argv[4])
