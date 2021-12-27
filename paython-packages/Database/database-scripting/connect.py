#!/usr/bin/env python

import MySQLdb as mdb
import sys

def connect_db():
    connect = mdb.connect(
        'localhost',
        'test_user',
        'test123'
    #    'test'
    )

    connection = connect.cursor()

    connection.execute("SELECT VERSION()")
    version = connection.fetchone()

    print("Database verion is: %s " % version)

    connection.close()

connect_db()
