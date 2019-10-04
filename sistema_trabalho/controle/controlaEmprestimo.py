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

    #abre a tela inicial de emprestimo
    def abre_tela_emprestimo(self):
        opcoes = {0: self.emprestar_veiculo, 1: self.devolver_veiculo, 2: self.listar_registros, 3: self.voltar}
        opcao = self.__tela_emprestimo.listar_opcoes()
        return opcoes[opcao]()

    # empresta veículos fazendo testes de permissão
    def emprestar_veiculo(self):
        matricula = self.__tela_emprestimo.retirar_veiculo()
        funcionarios = self.__sistema.controla_funcionario.funcionarios
        veiculos = self.__sistema.controla_veiculo.veiculos
        tela = self.__tela_emprestimo
        if matricula in funcionarios: #verifica se a matrícula existe
            funcionario = funcionarios[matricula]
            if funcionario.bloqueio >= 3: #verifica se funcionário está bloqueado
                funcionario.bloqueio += 1
                return self.registrar(veiculo, funcionario, 4)
            elif funcionario.cargo == 'DIRETOR' or funcionario.cargo == 'DIRETORA': #verifica se o cargo é de diretor(a)
                tela.listar_veiculos(veiculos) #lista os veiculos para a escolha
                placa = tela.pedir_placa()
                veiculo = veiculos[placa]
                self.verificar_emprestimo(veiculo, funcionario)
            else:
                if len(funcionario.veiculos) == 0: #testa de o funcionário não tem nenhum veículo com permissão
                    placa = tela.pedir_placa()
                    veiculo = veiculos[placa]
                    self.registrar(veiculo, funcionario, 2)
                    funcionario.bloqueio += 1
                    # fazer 3 tentativas bloquear
                elif len(funcionario.veiculos) == 1: #testa se o funcionário tem apenas um veículo com permissão
                    self.verificar_emprestimo(list(funcionario.veiculos.values())[0],funcionario)
                else:
                    tela.listar_veiculos(funcionario.veiculos) #lista os veiculos para a escolha
                    placa = tela.pedir_placa()
                    if placa in funcionario.veiculos:
                        veiculo = veiculos[placa]
                        self.verificar_emprestimo(veiculo,funcionario)
                    else:
                        veiculo = self.__sistema.controla_veiculo.veiculos[placa]
                        self.registrar(veiculo, funcionario, 2)
                        funcionario.bloqueio += 1
        else:
            self.registrar(None, None, 1)
        self.abre_tela_emprestimo()


    #verifica se o veívulo solicitado está ou não disponível e cria um registro
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
        self.abre_tela_emprestimo()

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
        elif filtro == 4: #voltar
            pass
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
        self.abre_tela_emprestimo()

    def validar_placa(self, placa):
        veiculos = self.__sistema.controla_veiculo.veiculos
        if placa in veiculos:
            return placa
        else:
            print('Placa inexistente')
            self.abre_tela_emprestimo()
