from abc import ABC, abstractclassmethod


class TelaAbstract(ABC):
    def verificar_inteiro(self, inteiros_validos: [] = None):
        while True:
            valor_lido = input()
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('Valor incorreto, digite uma opção válida')