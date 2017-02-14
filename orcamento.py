#-*- coding:UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Estado_de_um_orcamento(object):

    __metaclass__ = ABCMeta

    def __init__(self):
        self.desconto_aplicado = False

    @abstractmethod
    def aplica_desconto_extra(self, orcamento):
        pass


    @abstractmethod
    def aprova(self, orcamento):
        pass


    @abstractmethod
    def reprova(self, orcamento):
        pass


    @abstractmethod
    def finaliza(self, orcamento):
        pass


class Em_aprovacao(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.05)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')

    def aprova(self, orcamento):
        orcamento.estado_atual = Aprovado()


    def reprova(self, orcamento):
        orcamento.estado_atual = Reprovado()


    def finaliza(self, orcamento):
        raise Exception('Orcamentos em aprovação não podem ir para finalizados diretamente')


class Aprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        if not self.desconto_aplicado:
            orcamento.adiciona_desconto_extra(orcamento.valor * 0.02)
            self.desconto_aplicado = True
        else:
            raise Exception('Desconto já aplicado')



    def aprova(self, orcamento):
        raise Exception('Orçamento já está em estado de aprovação')


    def reprova(self, orcamento):
        raise Exception('Orçamento está em estado de aprovação e não pode ser reprovado')


    def finaliza(self, orcamento):
        orcamento.estado_atual = Finalizado()



class Reprovado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos reprovados não recebem desconto extra')


    def aprova(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser aprovado')


    def reprova(self, orcamento):
        raise Exception('Orçamento já está em estado de reprovação')


    def finaliza(self, orcamento):
        raise Exception('Orçamento reprovado não pode ser finalizado')


class Finalizado(Estado_de_um_orcamento):

    def aplica_desconto_extra(self, orcamento):
        raise Exception('Orçamentos finalizados não recebem desconto extra')


    def aprova(self, orcamento):
        raise Exception('Orçamento finalizado já foi aprovado')


    def reprova(self, orcamento):
        raise Exception('Orçamento já finalizado não pode ser reprovado')


    def finaliza(self, orcamento):
        raise Exception('Orçamento já foi finalizado')


class Orcamento(object):

    def __init__(self):
        self.__itens = []
        self.estado_atual = Em_aprovacao()
        self.__desconto_extra = 0


    def adiciona_desconto_extra(self, desconto):
        self.__desconto_extra += desconto


    def aplica_desconto_extra(self):
        self.estado_atual.aplica_desconto_extra(self)


    def aprova(self):
        self.estado_atual.aprova(self)


    def reprova(self):
        self.estado_atual.reprova(self)


    def finaliza(self):
        self.estado_atual.finaliza(self)


    @property
    def valor(self):
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total - self.__desconto_extra


    def obter_itens(self):
        return tuple(self.__itens)


    @property
    def total_itens(self):
        return len(self.__itens)


    def adiciona_item(self, item):
        self.__itens.append(item)


class Item(object):

    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor


    @property
    def valor(self):
        return self.__valor


    @property
    def nome(self):
        return self.__nome


if __name__ == '__main__':
    orcamento = Orcamento()
    print(orcamento.estado_atual.desconto_aplicado)


    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    print(orcamento.valor)
    orcamento.aplica_desconto_extra()

    print(orcamento.estado_atual.desconto_aplicado)

    print(orcamento.valor)
    orcamento.aprova()
    print(orcamento.estado_atual.desconto_aplicado)

    orcamento.aplica_desconto_extra()
    print(orcamento.estado_atual.desconto_aplicado)



    print(orcamento.valor)
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)


    orcamento.finaliza()
    print(orcamento.estado_atual.desconto_aplicado)


