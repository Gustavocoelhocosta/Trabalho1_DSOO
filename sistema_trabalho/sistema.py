from limite.telaInicial import TelaInicial
from controle.controlaEmprestimo import ControlaEmprestimo
from controle.controlaFuncionario import ControlaFuncionario
from controle.controlaVeiculo import ControlaVeiculo
from sistema_trabalho.entidade.veiculo import Veiculo
from sistema_trabalho.entidade.funcionario import Funcionario
from sistema_trabalho.entidade.registro import Registro


class Sistema():
    def __init__(self):
        self.__tela_inicial = TelaInicial()

        self.__controla_veiculo = ControlaVeiculo(self)
        v0 = Veiculo('mmm0000', 'onix', 'chevrolet', 2000, 15000)
        v1 = Veiculo('mmm0001', 'X1', 'BMW', 2000, 15000)
        v2 = Veiculo('mmm0002', 'K', 'Ford', 2000, 15000)
        self.__controla_veiculo.veiculos['mmm0001'] = v1
        self.__controla_veiculo.veiculos['mmm0000'] = v0
        self.__controla_veiculo.veiculos['mmm0002'] = v2

        self.__controla_funcionario = ControlaFuncionario(self)
        f0 = Funcionario(0, 'João', '07061984', '48988041793', 'Funcionario')
        f1 = Funcionario(1, 'Maria', '07061984', '48988041793', 'Diretor')
        f2 = Funcionario(2, 'José', '07061984', '48988041793', 'Operador')
        f3 = Funcionario(3, 'joelma', '07061984', '48988041793', 'Operador')
        self.__controla_funcionario.funcionarios[0] = f0
        self.__controla_funcionario.funcionarios[1] = f1
        self.__controla_funcionario.funcionarios[2] = f2
        self.__controla_funcionario.funcionarios[3] = f3
        self.__controla_funcionario.funcionarios[0].veiculos['mmm0000'] = v0
        self.__controla_funcionario.funcionarios[0].veiculos['mmm0001'] = v1
        self.__controla_funcionario.funcionarios[2].veiculos['mmm0002'] = v2

        self.__controla_emprestimo = ControlaEmprestimo(self)
        r0 = Registro(v1,f1,0)
        r1 = Registro(v2,f1,1)
        r2 = Registro(v2,f2,2)
        r3 = Registro(v0,f0,3)
        r4 = Registro(v0,f3,4)
        r5 = Registro(v1,f0,0)
        self.__controla_emprestimo.registros.append(r0)
        self.__controla_emprestimo.registros.append(r1)
        self.__controla_emprestimo.registros.append(r2)
        self.__controla_emprestimo.registros.append(r3)
        self.__controla_emprestimo.registros.append(r4)
        self.__controla_emprestimo.registros.append(r5)

       # self.chamar_tela_inicial()

    @property
    def controla_veiculo(self):
        return self.__controla_veiculo

    @property
    def controla_emprestimo(self):
        return self.__controla_emprestimo

    @property
    def controla_funcionario(self):
        return self.__controla_funcionario

    def chamar_tela_inicial(self):
        opcoes = {0: self.chamar_controla_veiculo, 1: self.chamar_controla_funcionario, 2: self.chamar_controla_emprestimo}
        opcao = self.__tela_inicial.listar_opcoes_sistema()
        return opcoes[opcao]()

    def chamar_controla_veiculo(self):
        self.__controla_veiculo.abre_tela_veiculo()

    def chamar_controla_emprestimo(self):
        self.__controla_emprestimo.abre_tela_emprestimo()


    def chamar_controla_funcionario(self):
        pass

    # def validar_inteiro(self, valor: int, validos: []):
    #     while not (isinstance(valor, int)) or not valor in validos:
    #         print('valor incorreto, digite um valor inteiro válido')
    #         try:
    #             valor = int(input())
    #         except:
    #             ValueError
    #     return valor



s = Sistema()


s.chamar_tela_inicial()


