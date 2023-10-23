#!/usr/bin/python3
"""Write a script that lists all states starting with N from hbtn_0e_0_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for i in range(len(states)):
        if states[i][1][0] == "N":
            print(states[i])
    cursor.close()
    db.close()
