from limite.telaInicial import TelaInicial
from controle.controlaEmprestimo import ControlaEmprestimo
from controle.controlaFuncionario import ControlaFuncionario
from controle.controlaVeiculo import ControlaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.entidade.funcionario import Funcionario


class Sistema():
    def __init__(self):
        self.__tela_inicial = TelaInicial()
        self.__controla_veiculo = ControlaVeiculo(self)
        self.__controla_veiculo.veiculos['mmm0000']= Veiculo('mmm0000', 'onix', 'chevrolet', 2000, 15000)
        self.__controla_veiculo.veiculos['mmm0001'] = Veiculo('mmm0000', 'onix', 'chevrolet', 2000, 15000)
        self.__controla_veiculo.veiculos['mmm0002'] = Veiculo('mmm0000', 'onix', 'chevrolet', 2000, 15000)
        self.__controla_emprestimo = ControlaEmprestimo(self)
        self.__controla_funcionario = ControlaFuncionario(self)
        self.__controla_funcionario.funcionarios[1] = Funcionario(1, 'João', '07061984', '48988041793', 'Funcionario')
        self.__controla_funcionario.funcionarios[2] = Funcionario(1, 'Maria', '07061984', '48988041793', 'Diretor')
        self.__controla_funcionario.funcionarios[3] = Funcionario(1, 'José', '07061984', '48988041793', 'Operador')


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
        opcoes = {0: self.chamar_controla_veiculo, 1: self.chamar_controla_funcionario, 2: self.chamar_controla_emprestimo}
        opcao = self.__tela_inicial.listar_opcoes_sistema()
        return opcoes[opcao]()

    def chamar_controla_veiculo(self):
        self.__controla_veiculo.abre_tela_veiculo()

    def chamar_controla_emprestimo(self):
        self.__controla_emprestimo.abre_tela_emprestimo()


    def chamar_controla_funcionario(self):
        pass

s = Sistema()

s.chamar_tela_inicial()

