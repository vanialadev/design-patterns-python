# -*- coding: UTF-8 -*-

class Soma(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() + self.__expressao_direita.avalia()


    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda


    @property
    def expressao_direita(self):
        return self.__expressao_direita


    def aceita(self, visitor):
        visitor.visita_soma(self)


class Subtracao(object):

    def __init__(self, expressao_esquerda, expressao_direita):
        self.__expressao_esquerda = expressao_esquerda
        self.__expressao_direita = expressao_direita

    def avalia(self):
        return self.__expressao_esquerda.avalia() - self.__expressao_direita.avalia()


    @property
    def expressao_esquerda(self):
        return self.__expressao_esquerda


    @property
    def expressao_direita(self):
        return self.__expressao_direita

    def aceita(self, visitor):
        visitor.visita_subtracao(self)


class Numero(object):

    def __init__(self, numero):
        self.__numero = numero


    def avalia(self):
        return self.__numero


    def aceita(self, visitor):
        visitor.visita_numero(self)



if __name__ == '__main__':

    from impressao import Impressao, Prefixa_visitor


    expressao_esquerda = Soma(Numero(10), Numero(5))
    expressao_direita = Soma(Numero(2), Numero(10))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    resultado = expressao_conta.avalia()
    print(resultado)

    impressao = Impressao()


    expressao_conta.aceita(impressao)

    expressao_esquerda = Subtracao(Numero(100), Numero(20))
    expressao_direita = Soma(Numero(5), Numero(5))
    expressao_conta = Soma(expressao_esquerda, expressao_direita)

    print('\n############')

    expressao_conta.aceita(impressao)


    prefixa_visitor = Prefixa_visitor()

    print('\n############')

    expressao_conta.aceita(prefixa_visitor)
