from controlaAbstract import ControlaAbstract
from sistema_trabalho.entidade.veiculo import Veiculo


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
        self.__tela_veiculo.listar_opcoes()



    def incluir_veiculo(self):
        dados_veiculo = self.__tela_veiculo.cadastrar_veiculo()
        placa = dados_veiculo[0]
        marca = dados_veiculo[1]
        modelo = dados_veiculo[2]
        ano = dados_veiculo[3]
        quilometragem_atual = dados_veiculo[4]

        if placa in self.__veiculos:
            print('veiculo já cadastrado')
        else:
            self.__veiculos[placa] = Veiculo(placa, modelo, marca, ano, quilometragem_atual)
            if not modelo in self.__modelos:
                self.__modelos.append(modelo)
            if not marca in self.__marcas:
                self.__marcas.append(marca)

    def excluir_veiculo(self):
        placa = self.__tela_veiculo.excluir_veiculo()
        if placa in self.__veiculos:
            del(self.__veiculos[placa])


