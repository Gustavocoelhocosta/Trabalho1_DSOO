from sistema_trabalho.limite.telaAbstract import TelaAbstract

class TelaInicial(TelaAbstract):
    def listar_opcoes_sistema(self):
        print('-----------------------------------------------')
        print('Escolha dentre as opções')
        print('0 - cadastro veículos')
        print('1 - cadastro funcionarios')
        print('2 - emprestimo veículos')
        valor = self.validar_inteiro(input('Digite o numero da opção escolhida - '), [0,1,2])
        return valor





