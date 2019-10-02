import sistema_trabalho.limite.telaAbstract

class TelaEmprestimo(sistema_trabalho.limite.telaAbstract.TelaAbstract):

    def listar_opcoes(self):
        opcoes = {0: self.cadastrar_veiculo, 1: self.excluir_veiculo, 2: self.listar_veiculos}
        print('Escolha dentre as opções')
        print('0 - retirar veículo')
        print('1 - devolver veículo')
        print('2 - listar registros')
        valor = int(input('Digite o numero da opção escolhida - '))
        return opcoes[valor]()


    def emprestar_veiculo(self):
        print('Emprestimo de veículo')
        dados = []
        dados.append(input('digite a matricula - '))
        dados.append(input('digite a placa - '))
        return dados


    def devolver_veiculo(self):
        print('Devolução de veículo')
        dados = []
        dados.append(input('digite a placa - '))
        dados.append(input('digite a quilometragem - '))
        return dados


    def listar_registros(self, lista):
        return print(lista)

