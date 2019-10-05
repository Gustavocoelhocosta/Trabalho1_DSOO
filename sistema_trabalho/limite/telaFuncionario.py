from sistema_trabalho.limite.telaAbstract import TelaAbstract


class TelaFuncionario(TelaAbstract):
    def listar_opcoes(self):
        print('Escolha dentre as opções')
        print('0 - incluir funcionário')
        print('1 - excluir funcionário')
        print('2 - listar funcionários')
        print('3 - voltar')
        opcao = self.validar_inteiro(input('Digite o numero da opção escolhida - '), [0,1,2,3])
        return opcao

    def cadastrar_funcionario(self):
        print('Cadastrar novo funcionário')
        dados = list()
        dados.append(self.inteiro(input('Digite a matrícula: ')))
        dados.append(input('Digite o nome: ').upper())
        dados.append(self.inteiro(input('Digite a data de nascimento (ddmmaaaa): ')))
        dados.append(self.inteiro(input('Digite o telefone: ')))
        dados.append(input('Digite o cargo: ').upper())
        return dados

    def pedir_matricula(self):
        return self.inteiro(input('Digite a matrícula: '))

    def listar_funcionarios(self, lista):
        print('MATRÍCULA - NOME - DATA NASCIMENTO - TELEFONE - CARGO')
        for funcionario in lista:
            print('%d - %s - %d - %d - %s'% lista[funcionario].matricula,
                                            lista[funcionario].nome,
                                            lista[funcionario].data_de_nascimento,
                                            lista[funcionario].telefone,
                                            lista[funcionario].cargo)


