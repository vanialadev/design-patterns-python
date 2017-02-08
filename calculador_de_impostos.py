from impostos import ISS, ICMS

class Calculador_de_imposto(object):

    def realiza_calculo(self, orcamento, imposto):

        imposto_calculado = imposto.calcula(orcamento)

        print(imposto_calculado)


if __name__== '__main__':

    from orcamento import Orcamento

    calculador = Calculador_de_imposto()

    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())

    #duck typing

