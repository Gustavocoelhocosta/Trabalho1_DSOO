class Veiculo():
    def __init__(self, placa: str, modelo: str, marca: str, ano: int,  quilometragem_atual: int):
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__quilometragem_atual = quilometragem_atual
        self.__emprestado = False

    @property
    def emprestado(self):
        return self.__emprestado

    @emprestado.setter
    def emprestado(self, emprestado):
        self.__emprestado = emprestado

    @property
    def placa(self):
        return self.__placa

    @placa.setter
    def placa(self, placa):
        self.__placa = placa

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo

    @property
    def marca(self):
        return self.__marca

    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def quilometragem_atual(self):
        return self.__quilometragem_atual

    @quilometragem_atual.setter
    def quilometragem_atual(self, quilometragem_atual):
        self.__quilometragem_atual = quilometragem_atual