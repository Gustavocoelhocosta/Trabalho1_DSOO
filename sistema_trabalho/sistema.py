from limite.telaInicial import TelaInicial
from controle.controlaEmprestimo import ControlaEmprestimo
from controle.controlaFuncionario import ControlaFuncionario
from controle.controlaVeiculo import ControlaVeiculo

class Sistema():
    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__controla_veiculo = ControlaEmprestimo()
        self.__controla_emprestimo = ControlaVeiculo()
        self.__controla_funcionario = ControlaFuncionario()

    @property
    def controla_veiculo(self):
        return self.__controla_veiculo

    @property
    def controla_emprestimo(self):
        return self.__controla_emprestimo

    @property
    def controla_funcionario(self):
        return self.__controla_funcionario