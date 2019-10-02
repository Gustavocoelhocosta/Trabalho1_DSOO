from limite.telaInicial import TelaInicial
from controle.controlaEmprestimo import ControlaEmprestimo
#from controle.controlaFuncionario import ControlaFuncionario
from controle.controlaVeiculo import ControlaVeiculo

class Sistema():
    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__controla_veiculo = ControlaVeiculo()
        self.__controla_emprestimo = ControlaEmprestimo()
#       self.__controla_funcionario = ControlaFuncionario()

    @property
    def controla_veiculo(self):
        return self.__controla_veiculo

    @property
    def controla_emprestimo(self):
        return self.__controla_emprestimo

    @property
    def controla_funcionario(self):
        return self.__controla_funcionario

    def chamar_tela_inicial(self):
        opcoes = {0: self.chamar_controla_veiculo, 1: self.chamar_controla_emprestimo, 2: self.chamar_controla_funcionario}
        opcao = self.__tela_inicial.listar_opcoes()
        return opcoes[opcao]()

    def chamar_controla_veiculo(self):
        self.__controla_veiculo.abre_tela_veiculo()
        pass

    def chamar_controla_emprestimo(self):
        self.__controla_emprestimo.abre_tela_emprestimo()

    def chamar_controla_funcionario(self):
        pass

s = Sistema()

s.chamar_tela_inicial()

