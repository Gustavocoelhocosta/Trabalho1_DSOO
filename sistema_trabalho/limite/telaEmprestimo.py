import sistema_trabalho.limite.telaAbstract

class TelaEmprestimo():
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
        dados.append(int(input('digite quilometros rodados - ')))
        return dados

    def listar_filtro_registro(self):
        print('Escolha o filtro do registro')
        print('0 - por motivo/permissão')
        print('1 - por matrícula do funcionario')
        print('2 - por placa do veículo')
        print('3 - todos os registros')
        filtro = int(input('Digite o numero da opção escolhida - '))
        if filtro == 0:
            print('Escolha o motivo')
            print('4 - Acesso permitido ao veiculo')
            print('5 - Matrícula não existe')
            print('6 - Não possui acesso ao veículo')
            print('7 - veículo indisponível')
            motivo = int(input('Digite o numero da opção escolhida - '))
            return [0, motivo]
        elif filtro == 1:
            #listar todos os funcionarios
            return [1, int(input('Digite a matrícula - '))]
        elif filtro == 2:
            #listar todas as placas
            return [2, input('Digite a placa - ')]
        else:
            return [filtro, None]

    def listar_registros(self, lista):
        for registro in lista:
            print('%s - %s - %s'% (registro.veiculo.placa, registro.funcionario.nome, registro.motivo))


    def listar_veiculos(self, lista):
        for veiculo in lista:
            print('%s - %s - %s - %d - %d'% (veiculo, lista[veiculo].modelo, lista[veiculo].marca, lista[veiculo].ano, lista[veiculo].quilometragem_atual))
