import telaAbstract import TelaAbstract


class TelaVeiculo(TelaAbstract):
    def __init__(self):
        pass

    def listar_opcoes(self):
        opcoes = {}


    def cadastrar_veiculo(self):
        print('Cadastrar novo veículo')
        dados = []
        dados.append(input('digite a placa'))
        dados.append(input('digite o modelo'))
        dados.append(input('digite a marca'))
        dados.append(int(input('digite o ano')))
        dados.append(input('digite a quilometragem atual'))
        return dados