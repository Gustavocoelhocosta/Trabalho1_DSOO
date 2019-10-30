from sistema_trabalho.limite.telaAbstract import TelaAbstract


class TelaVeiculo(TelaAbstract):
    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - incluir veículo')
        print('1 - excluir veículo')
        print('2 - listar veículos')
        print('3 - voltar')
        valor = self.validar_inteiro(input('Digite o numero da opção escolhida - '), [0,1,2,3])
        return valor

    def pedir_dados_veiculo(self):
        print('insira os dados do veículo')
        dados = []
        dados.append(self.validar_placa(input('digite a placa - ')))
        dados.append(input('digite o modelo - ').upper())
        dados.append(input('digite a marca - ').upper())
        dados.append(self.inteiro(input('digite o ano de fabricação - ')))
        dados.append(self.inteiro(input('digite a quilometragem atual - ')))
        return dados








