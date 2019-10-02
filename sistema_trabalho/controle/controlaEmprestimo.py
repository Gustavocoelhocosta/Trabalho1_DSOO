from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.telaEmprestimo import TelaEmprestimo


class ControlaEmprestimo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__registros = []
        self.__tela_emprestimo = TelaEmprestimo()

    @property
    def registros(self):
        return self.__registros

    @property
    def tela_emprestimo(self):
        return self.__tela_emprestimo

    def abre_tela_emprestimo(self):
        opcoes = {0: self.emprestar_veiculo, 1: self.devolver_veiculo, 2: self.listar_registros, 3: self.voltar}
        opcao = self.__tela_emprestimo.listar_opcoes()
        return opcoes[opcao]()

    def emprestar_veiculo(self):
        self.__tela_emprestimo.retirar_veiculo()


        self.abre_tela_emprestimo()

    def devolver_veiculo(self):
        self.__tela_emprestimo.devolver_veiculo()



        self.abre_tela_emprestimo()

    def listar_registros(self):




        self.abre_tela_emprestimo()

    def voltar(self):
        self.__sistema.chamar_tela_inicial()