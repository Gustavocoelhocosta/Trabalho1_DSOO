from controlaAbstract import ControlaAbstract
from veiculo import Veiculo


class ControlaVeiculo(ControlaAbstract):
    def __init__(self):
        self.__veiculos = {}
        self.__modelos = []
        self.__marcas = []
        self.__tela_veiculo = TelaVeiculo()

    @property
    def veiculos(self):
        return self.__veiculos

    @property
    def modelos(self):
        return self.__modelos

    @property
    def marcas(self):
        return self.__marcas

    def abre_tela_veiculo(self):
        retun self.__tela_veiculo

    #, placa: str, modelo: str, marca: str, ano: int,  quilometragem_atual: int
    def incluir_veiculo(self):
        dados_veiculo = self.__tela_veiculo.cadastrar_veiculo(self)
        placa = dados_veiculo[0]
        marca = dados_veiculo[1]
        modelo = dados_veiculo[2]
        ano = dados_veiculo[3]
        quilometragem_atual = dados_veiculo[4]



        if placa in self.__veiculos:
            pass
        else:
            self.__veiculos[placa] = Veiculo(placa, modelo, marca, ano, quilometragem_atual)
        if modelo in self.__modelos:
            pass
        else:
            self.__modelos.append(modelo)
        if marca in self.__marcas:
            pass
        else:
             self.__marcas.append(marca)

    def excluir_veiculo(self, placa):
        if placa in self.__veiculos:
            del(self.__veiculos[placa])


