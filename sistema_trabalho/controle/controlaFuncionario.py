from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.limite.telaFuncionario import TelaFuncionario
from sistema_trabalho.entidade.funcionario import Funcionario

class ControlaFuncionario(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__funcionarios = dict()
        self.__tela = TelaFuncionario()

    @property
    def funcionarios(self):
        return self.__funcionarios

    def voltar(self):
        return

    def abre_tela_funcionario(self):
        opcoes = {0: self.incluir_funcionario, 1: self.excluir_funcionario, 2: self.listar_funcionarios, 3: self.voltar}
        opcao = self.__tela.listar_opcoes()
        return opcoes[opcao]()

    def incluir_funcionario(self):
        dados_funcionario = self.__tela.cadastrar_funcionario()
        matricula = dados_funcionario[0]
        nome = dados_funcionario[1]
        data_de_nascimento = dados_funcionario[2]
        telefone = dados_funcionario[3]
        cargo = dados_funcionario[4]

        if matricula in self.__funcionarios:
            self.__tela.imprimir('Não foi possivel cadastrar pois já existe um funcionário com essa matrícula')
        else:
            self.__funcionarios[matricula] = Funcionario(matricula, nome, data_de_nascimento, telefone, cargo)
            self.__tela.imprimir('Funcionário cadastrador com sucesso!')
            self.abre_tela_funcionario()

    def excluir_funcionario(self):
        matricula = self.__tela.pedir_matricula()
        if matricula in self.__funcionarios:
            del(self.__funcionarios[matricula])
            self.__tela.imprimir('Funcionário exclído com sucesso')
        else:
            self.__tela.imprimir('Não foi possível excluir, matrícula inválida')
            self.abre_tela_funcionario()

    def listar_funcionarios(self):
        self.__tela.listar_funcionarios(self.__funcionarios)
        self.abre_tela_funcionario()
