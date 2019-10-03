from sistema_trabalho.controle.controlaAbstract import ControlaAbstract
from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.telaEmprestimo import TelaEmprestimo


class ControlaEmprestimo(ControlaAbstract):
    def __init__(self, sistema):
        self.__sistema = sistema
        self.__registros = []
        self.__tela_emprestimo = TelaEmprestimo()

    @property
    def registros(self):
        return self.__registros

    @property
    def tela_emprestimo(self):
        return self.__tela_emprestimo

    def abre_tela_emprestimo(self):
        opcoes = {0: self.emprestar_veiculo, 1: self.devolver_veiculo, 2: self.listar_registros, 3: self.voltar}
        opcao = self.__tela_emprestimo.listar_opcoes()
        return opcoes[opcao]()

    def emprestar_veiculo(self):
        matricula = self.__tela_emprestimo.retirar_veiculo()
        funcionarios = self.__sistema.controla_funcionario.funcionarios
        if matricula in funcionarios:
            funcionario = funcionarios[matricula]
            if funcionario.cargo == 'Diretor':
                self.__tela_emprestimo.listar_veiculos(self.__sistema.controla_veiculo.veiculos)
                placa = self.__tela_emprestimo.pedir_placa()
                veiculo = self.__sistema.controla_veiculo.veiculos[placa]
                self.verificar_emprestimo(veiculo, funcionario)
            else:
                if len(funcionario.veiculos) == 0:
                    self.registrar(None, funcionario, 2)
                elif len(funcionario.veiculos) == 1:
                    self.verificar_emprestimo(list(funcionario.veiculos.values())[0],funcionario)
                else:
                    self.__tela_emprestimo.listar_veiculos(funcionario.veiculos)
                    placa = self.__tela_emprestimo.pedir_placa()
                    if placa in funcionario.veiculos:
                        veiculo = funcionario.veiculos[placa]
                        self.verificar_emprestimo(veiculo,funcionario)
                    else:
                        self.registrar(None, funcionario, 2)
        else:
            self.registrar(None, None, 1)
        self.abre_tela_emprestimo()

    def verificar_emprestimo(self, veiculo, funcionario):
        if veiculo.emprestado:
            self.registrar(veiculo, funcionario, 3)
        else:
            veiculo.emprestado = True
            self.registrar(veiculo, funcionario, 0)


    def devolver_veiculo(self):
        dados = self.__tela_emprestimo.devolver_veiculo()
        dados[0] = placa
        dados[1] = quilometros_rodados


        self.abre_tela_emprestimo()


    def registrar(self, veiculo, funcionario, motivo):
        registro = Registro(veiculo, funcionario, motivo)
        self.__registros.append(registro)
        return print(registro.motivo)


    def listar_registros(self):
        filtro = self.__tela_emprestimo.listar_filtro_registro()[0]
        parametro = self.__tela_emprestimo.listar_filtro_registro()[1]
        registros_filtrados = []
        if filtro == 3:
            self.__tela_emprestimo.listar_registros(self.__registros)
        else:
            for registro in self.__registros:
                if filtro == 1: #filtra por matricula
                    matricula = registro.funcionario.matricula
                    if matricula == parametro:
                        registros_filtrados.append(registro)
                elif filtro == 2: #filtra por placa
                    placa = registro.veiculo.placa
                    if placa == parametro:
                        registros_filtrados.append(registro)
                else: #filtro por motivo
                    motivo = registro.motivo
                    if motivo == parametro:
                        registros_filtrados.append(registro)
            self.__tela_emprestimo.listar_registros(registros_filtrados)
            print('listou controle')
            self.abre_tela_emprestimo()

    def voltar(self):
        self.__sistema.chamar_tela_inicial()
