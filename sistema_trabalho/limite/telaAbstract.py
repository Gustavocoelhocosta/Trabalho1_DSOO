from abc import ABC, abstractclassmethod


class TelaAbstract(ABC):

    def imprimir(self, conteudo):
        print(conteudo)

    def listar_veiculos(self, lista):
        print('PLACA - MODELO - MARCA - ANO - QUILOMETRAGEM')
        for veiculo in lista:
            print('%s - %s - %s - %d - %d'% (lista[veiculo].placa, lista[veiculo].modelo, lista[veiculo].marca, lista[veiculo].ano, lista[veiculo].quilometragem_atual))

    def validar_inteiro(self, valor: int, validos: []):
        try:
            valor = int(valor)
            if not valor in validos:
                raise ValueError
            return valor
        except:
            while not (isinstance(valor, int)) or not valor in validos:
                print('valor incorreto, digite um valor inteiro válido')
                try:
                    valor = int(input())
                except:ValueError
            return valor


    def inteiro(self, valor):
        try:
            valor = int(valor)
            return valor
        except:
            while not (isinstance(valor, int)):
                print('valor incorreto, digite um valor inteiro válido')
                try:
                    valor = int(input())
                except:ValueError

    def validar_placa(self, placa):
        pafrao_placa = re.compile('^[A-Z]{3}\d{4}$')
        placa = placa.upper()
        if re.match(pafrao_placa, placa):
            return placa
        else:
            while not re.match(pafrao_placa, placa):
                print('Placa inválida')
                placa = input().upper()
            return placa
