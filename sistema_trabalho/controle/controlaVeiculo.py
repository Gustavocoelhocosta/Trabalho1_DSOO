from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.limite.telaVeiculo import TelaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo


class ControlaVeiculo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__veiculos = {}
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

#    def voltar(self):
#       return

    def abre_tela_veiculo(self):
        opcoes = {0: self.incluir_veiculo, 1: self.excluir_veiculo, 2: self.listar_veiculos, 3: self.voltar}
        opcao = self.__tela_veiculo.listar_opcoes()
        return opcoes[opcao]()

    def incluir_veiculo(self):
        dados_veiculo = self.__tela_veiculo.cadastrar_veiculo()
        placa = dados_veiculo[0]
        modelo = dados_veiculo[1]
        marca = dados_veiculo[2]
        ano = dados_veiculo[3]
        quilometragem_atual = dados_veiculo[4]

        if placa in self.__veiculos:
            self.__tela_veiculo.imprimir('não foi possivel cadastrar pois já existe veículo com essa placa')
        else:
            self.__veiculos[placa] = Veiculo(placa, modelo, marca, ano, quilometragem_atual)
            self.__tela_veiculo.imprimir('veiculo cadastrado com sucesso')
        self.abre_tela_veiculo()


    def excluir_veiculo(self):
        placa = self.__tela_veiculo.pedir_placa()
        placa = self.validar_veiculo(placa)
        del(self.__veiculos[placa])
        self.__tela_veiculo.imprimir('veículo excluido com sucesso')
        self.abre_tela_veiculo()


    def listar_veiculos(self):
        lista = self.__veiculos
        self.__tela_veiculo.listar_veiculos(lista)
        self.abre_tela_veiculo()

    def voltar(self):
        self.__sistema.chamar_tela_inicial()


    def validar_veiculo(self, placa):
        if placa in self.veiculos:
            return placa
        else:
            print('Veículo não cadastrado')
            return self.validar_veiculo(self.__tela_veiculo.pedir_placa())