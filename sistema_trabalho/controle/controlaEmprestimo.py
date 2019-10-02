from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.telaEmprestimo import TelaEmprestimo

class ControlaEmprestimo(ControlaAbstract):
    def __init__(self):
        self.__registros = {}
        self.__tela_emprestimo = TelaEmprestimo()

    @property
    def registros(self):
        return self.__registros

    @property
    def tela_emprestimo(self):
        return self.__tela_emprestimo

    def abre_tela_emprestimo(self):
        return self.__tela_emprestimo.listar_opcoes()

    def emprestar_veiculo(self):
        dados = self.__tela_emprestimo.emprestar_veiculo()
        matricula = dados[0]
        placa = dados[1]
        return Print('Acesso Permitido ao Veículo')

    def devolver_veiculo(self):
        dados = self.__tela_emprestimo.devolver_veiculo()
        placa = dados[0]
        quilometragem = dados[1]

        return Print('Veículo devolvido')

    def listar_registros(self):
        lista = self.__registros
        self.__tela_emprestimo.listar_registros(lista)
