#!/usr/bin/python3
"""takes in the name of a state as an arg & lists all cities of the state"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
            LEFT JOIN states ON cities.state_id = states.id \
            WHERE BINARY states.name = %s \
            ORDER BY cities.id ASC", (sys.argv[4],))
    cities = cursor.fetchall()
    c_list = []
    for city in cities:
        c_list.append(city[0])
    print(", ".join(c_list))
    cursor.close()
    db.close()
