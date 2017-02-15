# -*- coding: UTF-8 -*-

import MySQLdb

class Connection_Factory(object):

    def get_connection(self):
        connection = MySQLdb.connect(
            host='localhost',
            user='root',
            password='',
            db='alura'
        )
        return connection

