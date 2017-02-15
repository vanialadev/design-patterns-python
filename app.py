# -*- coding: UTF-8 -*-
import MySQLdb
from connection_factory import get_connection

# connection=MySQLdb.connect(
#         host='localhost',
#         user='root',
#         password='',
#         db='alura'
# )

connection = get_connection()

cursor = connection.cursor()

cursor.execute('SELECT * FROM cursos')

for linha in cursos:
    print(linha)

connection.close()


#exemplo do design patterns Factory, nao é mesmo uma conexão com o bd