# -*- coding: UTF-8 -*-

def imprime_com_destaque(metodo):
    def wrapper(frase):
        print('*****')
        metodo(frase)
        print('*****')
    return wrapper


@imprime_com_destaque
def imprime(frase):
    print(frase)


if __name__ == '__main__':

    imprime('olá mundo!')
