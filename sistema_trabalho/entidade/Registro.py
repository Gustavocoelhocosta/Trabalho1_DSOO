from sistema_trabalho.entidade.funcionario import Funcionario
from sistema_trabalho.entidade.veiculo import Veiculo
import datetime

class Registro():
    def __init__(self, veiculo: Veiculo, funcionario: Funcionario):
        self.__veiculo = veiculo
        self.__funcionario = funcionario
        self.__data_hora = datetime.datetime.now()

    @property
    def veiculo(self):
        return self.__veiculo

    @property
    def funcionario(self):
        return self.__funcionario

    @property
    def data_hora(self):
        return self.__data_hora