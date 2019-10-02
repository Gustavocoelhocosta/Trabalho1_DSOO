import sistema_trabalho.limite.telaAbstract

class TelaEmprestimo(sistema_trabalho.limite.telaAbstract.TelaAbstract):

    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - retirar veículo')
        print('1 - devolver veículo')
        print('2 - listar registros')
        print('3 - voltar')
        valor = int(input('Digite o numero da opção escolhida - '))
        return valor


    def retirar_veiculo(self):
        print('Emprestimo de veículo')
        dados = []
        dados.append(input('digite a matricula - '))
        return dados


    def devolver_veiculo(self):
        print('Devolução de veículo')
        dados = []
        dados.append(input('digite a placa - '))
        dados.append(input('digite a quilometragem - '))
        return dados


    def listar_registros(self, lista):
        return print(lista)

