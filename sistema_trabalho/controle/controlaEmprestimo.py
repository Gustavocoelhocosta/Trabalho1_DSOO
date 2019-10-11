from sistema_trabalho.entidade.registro import Registro
from sistema_trabalho.limite.telaEmprestimo import TelaEmprestimo
#

class ControlaEmprestimo():
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

    #abre a tela inicial de emprestimo
    def abrir_tela_emprestimo(self):
        opcoes = {0: self.emprestar_veiculo, 1: self.devolver_veiculo, 2: self.listar_registros, 3: self.voltar}
        opcao = self.__tela_emprestimo.listar_opcoes()
        return opcoes[opcao]()

    #empresta os veiculos
    def emprestar_veiculo(self):
        matricula = self.__tela_emprestimo.pedir_matricula()
        funcionarios = self.__sistema.controla_funcionario.funcionarios
        veiculos = self.__sistema.controla_veiculo.veiculos
        tela = self.__tela_emprestimo
        tela.listar_veiculos(veiculos)  # lista os veiculos para a escolha
        placa = self.validar_veiculo(self.__tela_emprestimo.pedir_placa())
        veiculo = veiculos[placa]
        if not matricula in funcionarios:
            self.registrar(veiculo, None, 1)
            return self.abrir_tela_emprestimo()
        else:
            funcionario = funcionarios[matricula]
            if funcionario.cargo == 'DIRETOR' or funcionario.cargo == 'DIRETORA':
                self.verificar_emprestimo(veiculo, funcionario)
                return self.abrir_tela_emprestimo()
            elif funcionario.bloqueio > 2:
                self.registrar(veiculo, funcionario, 4)
                return self.abrir_tela_emprestimo()
            else:
                if veiculo in funcionario.veiculos:
                    self.verificar_emprestimo(veiculo, funcionario)
                    return self.abrir_tela_emprestimo()
                else:
                    self.registrar(veiculo, funcionario, 2)
                    funcionario.bloqueio += 1
                    return self.abrir_tela_emprestimo()
        self.abrir_tela_emprestimo()


    #verifica se o veículo solicitado está ou não disponível e cria um registro
    def verificar_emprestimo(self, veiculo, funcionario):
        if veiculo.emprestado:
            self.registrar(veiculo, funcionario, 3)
        else:
            veiculo.emprestado = True
            self.registrar(veiculo, funcionario, 0)

    #devolve o veículo mutando o status de emprestado para disponivel e atualiza a quilometragem
    def devolver_veiculo(self):
        dados = self.__tela_emprestimo.devolver_veiculo()
        placa = dados[0]
        quilometros_rodados = dados[1]
        veiculo = self.__sistema.controla_veiculo.veiculos[placa]
        veiculo.quilometragem_atual += quilometros_rodados
        veiculo.emprestado = False
        self.abrir_tela_emprestimo()

    #cria um registro e armazena na lista registros
    def registrar(self, veiculo, funcionario, motivo):
        registro = Registro(veiculo, funcionario, motivo)
        self.__registros.append(registro)
        self.__tela_emprestimo.imprimir(registro.motivo)

    #lista os registros por filtros
    def listar_registros(self):
        dados = self.__tela_emprestimo.listar_filtro_registro()
        filtro = dados[0]
        parametro = dados[1]
        registros_filtrados = []
        if filtro == 3: #lista todos os registros
            self.__tela_emprestimo.listar_registros(self.__registros)
            return self.abrir_tela_emprestimo()
        elif filtro == 4: #voltar
            return self.abrir_tela_emprestimo()
        else:
            for registro in self.__registros: #percorre todos os registros
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
        self.abrir_tela_emprestimo()

    def voltar(self):
        self.__sistema.chamar_tela_inicial()

    def validar_veiculo(self, placa):
        if placa in self.__sistema.controla_veiculo.veiculos:
            return placa
        else:
            print('Veículo não cadastrado')
            return self.validar_veiculo(self.__tela_emprestimo.pedir_placa())