# -*- coding: UTF-8 -*-

import MySQLdb

def get_connection():
    connection = MySQLdb.connect(
        host='localhost',
        user='root',
        password='',
        db='alura'
    )
    return connection

