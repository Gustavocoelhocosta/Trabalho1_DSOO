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
        opcoes[opcao]()
        self.__tela_veiculo.imprimir('---------------------------------------------------')
        return self.abrir_tela_veiculo()

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

    def excluir_veiculo(self):
        self.listar_veiculos()
        placa = self.__tela_veiculo.pedir_placa()
        if self.buscar_veiculo_placa(placa):
            veiculo = self.buscar_veiculo_placa(placa)
            if veiculo.emprestado:
                self.__tela_veiculo.imprimir('veículo fora da garagem')
            else:
                del self.veiculos[placa]
                self.__sistema.controla_funcionario.excluir_veiculo_funcionarios(placa)
                self.__tela_veiculo.imprimir('veículo excluido com sucesso')
        else:
            self.__tela_veiculo.imprimir('veículo inexistente')

        # placa = self.validar_veiculo(placa)
        # del(self.__veiculos[placa]) #e
        # funcionarios = self.__sistema.controla_funcionario.funcionarios
        # for funcionario in funcionarios.values():
        #     if placa in funcionario.veiculos:
        #         del(funcionario.veiculos[placa])
        # self.__tela_veiculo.imprimir('veículo excluido com sucesso')

    def listar_veiculos(self):
        lista = self.__veiculos
        self.__tela_veiculo.listar_veiculos(lista)

    def buscar_veiculo_placa(self, placa):
        if placa in self.__veiculos:
            return self.__veiculos[placa]
        else:
            return None

    def voltar(self):
        self.__sistema.chamar_tela_inicial()



