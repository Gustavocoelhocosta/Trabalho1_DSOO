class ControlaFuncionario():
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__funcionarios = dict()

 #       self.__tela = TelaFuncionario


    @property
    def funcionarios(self):
        return self.__funcionarios

    # def abre_tela_funcionario(self):
    #     pass
    #
    # def incluir_funcionario(self):
    #     dados = self.__tela.cadastra
    #
