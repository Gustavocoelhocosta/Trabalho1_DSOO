

class TelaInicial():
    def __init__(self):
        pass

    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - cadastro veículos')
        print('1 - cadastro funcionarios')
        print('2 - emprestimo veículos')
        valor = int(input('Digite o numero da opção escolhida - '))
        return valor