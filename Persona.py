class Persona():
    #Constructor por defecto
    #def __init__(self, nombre=):

    #Constructor con el nombre, edad, sexo, resto por defecto

    #Constructor con parametros
    def __init__(self, DNI, nombre="", edad=0, sexo="", peso=0.0, altura=0.0):
        self.__nombre = nombre
        self.__edad = edad
        self.__DNI = DNI
        self.__sexo = sexo
        self.__peso = peso
        self.__altura = altura

    #getter
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_sexo(self):
        return self.__sexo

    def get_peso(self):
        return self.__peso

    def get_altura(self):
        return self.__altura 

    #setter
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        self.__edad = edad

    def set_sexo(self, sexo):
        self.__sexo = sexo

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    def calcularIMC(self):
        MENOR = -1
        NORMAL = 0
        MAYOR = 1

        imc = float(self.get_peso()) / float(self.get_altura()) ** 2

        if imc < 20:
            resultado = MENOR
        elif imc < 25:
            resultado = NORMAL
        else:
            resultado = MAYOR
        return resultado
    
    def esMayorDeEdad(self):
        if int(self.get_edad()) >= 18:
            return True
        else:
            return False
    
    def comprobarSexo(self, sexo):
        genero = self.get_sexo().lower() 
        if  genero == "m":
            self.set_sexo("M")
        else:
            self.set_sexo("H")
    
    def __str__(self):
        return "Nombre: {}\nEdad: {}\nIdentificación: {}\nSexo: {}\nPeso: {}\nAltura: {}".format(self.__nombre, self.__edad, self.__DNI, self.__sexo, self.__peso, self.__altura)



