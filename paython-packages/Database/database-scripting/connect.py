#!/usr/bin/env python

import MySQLdb as mdb
import sys

def connect_db():
    connect = mdb.connect(
        '70.34.211.126',
        'root',
        'Ng}4NW@JDnaBautH',
        'mysql'
    )

    connection = connect.cursor()

    connection.execute("SELECT VERSION()")
    version = connection.fetchone()

    print("Database verion is: %s " % version)

    connection.close()

connect_db()
