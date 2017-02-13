#-*- coding:UTF-8 -*-

class Orcamento(object):

    EM_APROVACAO = 1
    APROVADO = 2
    REPROVADO = 3
    FINALIZADO = 4

    def __init__(self):
        self.__itens = []
        self.estado_atual = Orcamento.EM_APROVACAO
        self.__desconto_extra = 0


    def aplica_desconto_extra(self):

        if self.estado_atual == Orcamento.EM_APROVACAO:
            self.__desconto_extra += self.valor * 0.02
        elif self.estado_atual == Orcamento.APROVADO:
            self.__desconto_extra += self.valor * 0.05
        elif self.estado_atual == Orcamento.REPROVADO:
            raise Exception('Orçamentos reprovados não recebem desconto extra')
        elif self.estado_atual == Orcamento.FINALIZADO:
            raise Exception('Orçamentos finalizados não recebem desconto extra')


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

    orcamento.adiciona_item(Item('ITEM - 1', 100))
    orcamento.adiciona_item(Item('ITEM - 2', 50))
    orcamento.adiciona_item(Item('ITEM - 3', 400))

    print(orcamento.valor)
    orcamento.aplica_desconto_extra()
    print(orcamento.valor)

    orcamento.estado_atual = Orcamento.APROVADO
    orcamento.aplica_desconto_extra()
    print('Valor com desconto extra (aprovado) %s' % (orcamento.valor))