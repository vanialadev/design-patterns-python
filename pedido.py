# -*- coding: UTF-8 -*-
from datetime import date

class Pedido(object):

    def __init__(self, cliente, valor):
        self.__cliente = cliente
        self.__valor = valor
        self.__status = 'NOVO'
        self.__data_de_finalizacao = None

    def paga(self):
        self.__status = 'PAGO'

    def finaliza(self):
        self.__data_de_finalizacao = date.today()
        self.__status = 'ENTREGUE'

    @property
    def cliente(self):
        return self.__cliente

    @property
    def valor(self):
        return self.__valor

    @property
    def status(self):
        return self.__status

    @property
    def data_de_finalizacao(self):
        return self.__data_de_finalizacao

from abc import ABCMeta, abstractmethod
class Comando(object):

    __metaclass__ = ABCMeta

    @abstractmethod
    def executa(self):
        pass


class Paga_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.paga()


class Conclui_pedido(Comando):

    def __init__(self, pedido):
        self.__pedido = pedido

    def executa(self):
        self.__pedido.finaliza()

class Fila_de_trabalho(object):

    def __init__(self):
        self.__comandos =[]

    def adiciona(self, comando):
        self.__comandos.append(comando)

    def  processa(self):
        for comando in self.__comandos:
            comando.executa()



if __name__ == '__main__':

    pedido1 = Pedido('Flavio', 200)
    pedido2 = Pedido('Almeida', 400)

    fila_de_trabalho = Fila_de_trabalho()

    comando1 = Paga_pedido(pedido1)
    comando2 = Conclui_pedido(pedido1)
    comando3 = Paga_pedido(pedido2)



    fila_de_trabalho.adiciona(comando1)
    fila_de_trabalho.adiciona(comando2)
    fila_de_trabalho.adiciona(comando3)

    fila_de_trabalho.processa()

    print('Pedido 1, cliente', pedido1.cliente)
    print('Pedido 2 nao finalizado', pedido2.data_de_finalizacao)
    print('Pedido 1 finalizado', pedido1.data_de_finalizacao)
    print('Pedido 1 status', pedido1.status)
    print('Pedido 2 nao finalizado status', pedido2.status)