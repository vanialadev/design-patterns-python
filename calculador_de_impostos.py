from impostos import calcula_ISS, calcula_ICMS

class Calculador_de_imposto(object):

    def realiza_calculo(self, orcamento, imposto):

        # if imposto == 'ISS':
        #     # imposto_calculado = orcamento.valor * 0.1
        #     imposto_calculado = calcula_ISS(orcamento)
        #
        # elif imposto == 'ICMS':
        #     # imposto_calculado = orcamento.valor * 0.06
        #     imposto_calculado = calcula_ICMS(orcamento)

        imposto_calculado = imposto(orcamento)

        print(imposto_calculado)


if __name__== '__main__':

    from orcamento import Orcamento

    calculador = Calculador_de_imposto()

    orcamento = Orcamento(500)

    # calculador.realiza_calculo(orcamento, 'ISS')
    calculador.realiza_calculo(orcamento, calcula_ISS)
    calculador.realiza_calculo(orcamento, calcula_ICMS)

    #pattern Strategy

