from telaAbstract import TelaAbstract


class TelaVeiculo(TelaAbstract):
    def listar_opcoes(self):
        opcoes = {0: self.cadastrar_veiculo, 1: self.excluir_veiculo, 2: self.listar_veiculos}
        print('Escolha dentre as opções e digite o número referente')
        print('0 - cadastrar veículo')
        print('1 - excluir veículo')
        print('2 - listar veículos')
        opcao_escolhida = verificar_inteiro([0,1,2])
        if isinstance(opcao_escolhida, int):
            return  opcoes[opcao_escolhida]()
        return opcao_escolhida

    def cadastrar_veiculo(self):
        print('Cadastrar novo veículo')
        dados = []
        dados.append(input('digite a placa'))
        dados.append(input('digite o marca'))
        dados.append(input('digite a modelo'))
        dados.append(int(input('digite o ano')))
        dados.append(input('digite a quilometragem atual'))
        return dados

    def excluir_veiculo(self):
        print('Excluir veículo')
        placa = input('digite a placa do carro')
        return placa

    def listar_veiculos(self):
        pass