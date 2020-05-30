class Contador():
    #Constructor por defecto
    """def __init__(self):
        self.__valor = 0
        self.__frecuencia = 1"""
    #Constructor con parametros
    def __init__(self, valor=0, frecuencia=1):
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

    def incrementar(self):
        resultado =  self.get_valor() + self.get_frecuencia()
        print(resultado)
        return self.set_valor(resultado)

    def decrementar(self):
        resultado = self.get_valor() - self.get_frecuencia()
        print(resultado)
        return self.set_valor(resultado)
        


