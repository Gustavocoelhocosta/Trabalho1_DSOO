

class Funcionario():
    def __init__(self, matricula: int, nome: str, data_de_nascimento: str, telefone: int, cargo: str):
        self.__matricula = matricula
        self.__nome = nome
        self.__data_de_nascimento = data_de_nascimento
        self.__telefone = telefone
        self.__cargo = cargo
        self.__veiculos_permitidos = dict()

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @property
    def data_de_nascimento(self):
        return self.__data_de_nascimento

    @data_de_nascimento.setter
    def data_de_nascimento(self, data_de_nascimento: str):
        self.__data_de_nascimento = data_de_nascimento

    @property
    def telefone(self):
        return self.__telefone

    @telefone.setter
    def telefone(self, telefone: int):
        self.__telefone = telefone

    @property
    def cargo(self):
        return self.__cargo

    @cargo.setter
    def cargo(self, cargo):
        self.__cargo = cargo