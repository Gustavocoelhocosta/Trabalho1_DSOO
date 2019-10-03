from abc import ABC, abstractclassmethod


class ControlaAbstract(ABC):

    def voltar(self):
        self.__sistema.chamar_tela_inicial()