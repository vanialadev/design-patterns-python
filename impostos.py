from abc import ABCMeta, abstractmethod

class Imposto(object):
    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if (self.__outro_imposto is None):
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

class Template_de_imposto_condicional(Imposto):

    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.deve_cobrar_taxacao_maxima(orcamento):
            return self.taxacao_maxima(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.taxacao_minima(orcamento) + self.calculo_do_outro_imposto(orcamento)


    @abstractmethod
    def deve_cobrar_taxacao_maxima(self, orcamento):
        pass


    @abstractmethod
    def taxacao_maxima(self, orcamento):
        pass


    @abstractmethod
    def taxacao_minima(self, orcamento):
        pass

def IPVX(metodo_ou_funcao):
    def wrapper(self, orcamento):
        return metodo_ou_funcao(self, orcamento) + 50
    return wrapper


class ISS(Imposto):

    @IPVX
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)


class ICMS(Imposto):

    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)


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
