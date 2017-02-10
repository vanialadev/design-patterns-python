from abc import ABCMeta, abstractmethod
class Template_de_imposto_condicional(object):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_cobrar_taxacao_maxima(orcamento):
            return self.taxacao_maxima(orcamento)
        else:
            return self.taxacao_minima(orcamento)


    @abstractmethod
    def deve_cobrar_taxacao_maxima(self, orcamento):
        pass


    @abstractmethod
    def taxacao_maxima(self, orcamento):
        pass


    @abstractmethod
    def taxacao_minima(self, orcamento):
        pass


class ISS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(object):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class ICPP(Template_de_imposto_condicional):

    def deve_cobrar_taxacao_maxima(self, orcamento):
        return orcamento.valor > 500


    def  taxacao_maxima(self, orcamento):
        return orcamento.valor * 0.07


    def taxacao_minima(self, orcamento):
        return orcamento.valor * 0.05


class IKCV(Template_de_imposto_condicional):

    def  deve_cobrar_taxacao_maxima(self, orcamento):
        return orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento)

    def taxacao_maxima(self, orcamento):
        return orcamento.valor * 0.1

    def taxacao_minima(self, orcamento):
        return orcamento.valor *0.06


    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obter_itens():
            if item.valor > 100:
                return True
        return False
