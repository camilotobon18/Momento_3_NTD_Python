class Contador():
    #Constructor por defecto
    """def __init__(self):
        self.__valor = 0
        self.__frecuencia = 1"""
    #Constructor con parametros
    def __init__(self, valor, frecuencia):
        self.__valor = valor
        self.__frecuencia = frecuencia
    #Constructor copia

    #getter
    def get_valor(self):
        return self.__valor

    def get_frecuencia(self):
        return self.__frecuencia

    #setter
    def set_valor(self, valor):
        self.__valor = valor
    
    def set_frecuencia(self, frecuencia):
        self.__frecuencia = frecuencia

    
    """
    @property
    def incrementar(self):
        return self.

    @incrementar.setter
    def set_incrementar
        self.valor = self.valor + frecuencia
    """

contar = Contador()

contar.get_frecuencia()