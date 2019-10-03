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
        return int((input('digite a matricula - ')))

    def pedir_placa(self):
        return (input('digite a placa - '))

    def devolver_veiculo(self):
        print('Devolução de veículo')
        dados = []
        dados.append(input('digite a placa - '))
        dados.append(input('digite a quilometragem - '))
        return dados


    def listar_registros(self, lista):
        return print(lista)

    def listar_veiculos(self, lista):
        for veiculo in lista:
            print('%s - %s - %s - %d - %d'% (veiculo, lista[veiculo].modelo, lista[veiculo].marca, lista[veiculo].ano, lista[veiculo].quilometragem_atual))