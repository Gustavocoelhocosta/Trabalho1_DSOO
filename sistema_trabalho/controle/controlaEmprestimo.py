from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.telaRegistro import TelaRegistro
from sistema_trabalho.limite.telaEmprestimo import TelaEmprestimo

class ControlaEmprestimo(ControlaAbstract):
    def __init__(self):
        self.__registros = {}
        self.__tela_registro = TelaRegistro()
        self.__tela_emprestimo = TelaEmprestimo()

    @property
    def registros(self):
        return self.__registros



    def empresta_veiculo(self):
        dados = self.__tela_emprestimo.emprestar_veiculo()
        matricula = dados[0]
        placa = dados[1]


    def devolve_veiculo(self):
        pass
