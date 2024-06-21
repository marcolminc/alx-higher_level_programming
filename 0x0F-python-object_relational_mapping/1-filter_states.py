#!/usr/bin/python3
"""
Module "lists all states with a name starting with N (upper N) from the database
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
        if row[1][0] == 'N':
            print(row)


    db.close()


# usage:
if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    list_states(username, password, database)
