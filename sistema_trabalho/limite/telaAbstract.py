from abc import ABC, abstractclassmethod


class TelaAbstract(ABC):

    def imprimir(self, conteudo):
        print(conteudo)

    def listar_veiculos(self, lista):
        for veiculo in lista:
            print('%s - %s - %s - %d - %d'% (lista[veiculo].placa, lista[veiculo].modelo, lista[veiculo].marca, lista[veiculo].ano, lista[veiculo].quilometragem_atual))

    def validar_inteiro(self, valor: int, validos: []):
        try:
            valor = int(valor)
            if not valor in validos:
                raise
            return valor
        except:
            while not (isinstance(valor, int)) or not valor in validos:
                print('valor incorreto, digite um valor inteiro válido')
                try:
                    valor = int(input())
                except:ValueError
            return valor
