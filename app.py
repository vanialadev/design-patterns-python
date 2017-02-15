# -*- coding: UTF-8 -*-

from connection_factory import Connection_Factory

connection = Connection_Factory().get_connection()

cursor = connection.cursor()

cursor.execute('SELECT * FROM cursos')

for linha in cursos:
    print(linha)

connection.close()


#exemplo do design patterns Factory, nao é mesmo uma conexão com o bd