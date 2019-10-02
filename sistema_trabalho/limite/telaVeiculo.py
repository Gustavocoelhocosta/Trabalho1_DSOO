#from telaAbstract import TelaAbstract


class TelaVeiculo():
    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - incluir veículo')
        print('1 - excluir veículo')
        print('2 - listar veículos')
        print('3 - voltar')
        valor = int(input('Digite o numero da opção escolhida - '))
        return valor

    def cadastrar_veiculo(self):
        print('Cadastrar novo veículo')
        dados = []
        dados.append(input('digite a placa - '))
        dados.append(input('digite o marca - '))
        dados.append(input('digite a modelo - '))
        dados.append(int(input('digite o ano de fabricação - ')))
        dados.append(input('digite a quilometragem atual - '))
        return dados

    def excluir_veiculo(self):
        print('Excluir veículo')
        placa = input('digite a placa do veículo - ')
        return placa

    def listar_veiculos(self, lista):
        print(lista)