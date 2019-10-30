from sistema_trabalho.limite.telaVeiculo import TelaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo


class ControlaVeiculo():
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__veiculos = {}
        self.__tela_veiculo = TelaVeiculo()

    @property
    def veiculos(self):
        return self.__veiculos

    def abrir_tela_veiculo(self):
        opcoes = {0: self.incluir_veiculo, 1: self.excluir_veiculo, 2: self.listar_veiculos, 3: self.voltar}
        opcao = self.__tela_veiculo.listar_opcoes()
        return opcoes[opcao]()

    def incluir_veiculo(self):
        self.__tela_veiculo.imprimir('cadastro de novo veiculo')
        dados_veiculo = self.__tela_veiculo.pedir_dados_veiculo()
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
        self.abrir_tela_veiculo()

    def excluir_veiculo(self):
        placa = self.__tela_veiculo.pedir_placa()
        placa = self.validar_veiculo(placa)
        del(self.__veiculos[placa]) #e
        funcionarios = self.__sistema.controla_funcionario.funcionarios
        for funcionario in funcionarios.values():
            if placa in funcionario.veiculos:
                del(funcionario.veiculos[placa])
        self.__tela_veiculo.imprimir('veículo excluido com sucesso')
        self.abrir_tela_veiculo()

    # def alterar_veiculo(self):
    #     self.__tela_veiculo.imprimir('alterar veículo')
    #     self.listar_veiculos()
    #     opcoes = {0: self.incluir_veiculo, 1: self.excluir_veiculo, 2: self.listar_veiculos, 3: self.voltar}
    #     placa = self.__tela_veiculo.pedir_placa()
    #     veiculos = self.__veiculos
    #     placa = self.__tela_veiculo.pedir_placa()
    #     dados_veiculo = self.__tela_veiculo.self.__tela_veiculo.pedir_dados_veiculo()
    #     veiculos[dados_veiculo[0]] = veiculos[placa]
    #     veiculo.placa(dados_veiculo[0])
    #     5869.(dados_veiculo[1])
    #     veiculo.marca(dados_veiculo[2])
    #     veiculo.ano(dados_veiculo[3])
    #     veiculo.quilometragem_atual(dados_veiculo[4])

    def listar_veiculos(self):
        lista = self.__veiculos
        self.__tela_veiculo.listar_veiculos(lista)
        self.abrir_tela_veiculo()


    def buscar_veiculo_placa(self, placa):
        for veiculo in self.__veiculos:
            if placa == veiculo.placa:
                return veiculo
            else:
                return None

    def validar_veiculo(self, placa):
        if placa in self.veiculos:
            return placa
        else:
            print('Veículo não cadastrado')
            return self.validar_veiculo(self.__tela_veiculo.pedir_placa())

    def voltar(self):
        self.__sistema.chamar_tela_inicial()



