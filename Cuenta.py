class Cuenta():
    def __init__(self, cedula, nombre, fecha_apertura, cantidad=0.0):
        self.__cedula = cedula
        self.__nombre = nombre
        self.__fecha_apertura = fecha_apertura
        self.__cantidad = cantidad
    
    #getter
    def get_cedula(self):
        return self.__cedula

    def get_nombre(self):
        return self.__nombre
    
    def get_fecha_apertura(self):
        return self.__fecha_apertura

    def get_cantidad(self):
        return self.__cantidad

    #setter
    def set_cedula(self, cedula):
        self.__cedula = cedula
    
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_fecha_apertura(self, fecha_apertura):
        self.__fecha_apertura = fecha_apertura

    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad

    cantidad = property(get_cantidad, set_cantidad)
    
    #Metodo. ingresar(double cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, no se hará nada
    def ingresar(self, valor):
        while(True):
            try:
                valor = float(valor)
                if valor > 0:
                    resultado = float(self.get_cantidad()) + valor
                    return self.set_cantidad(resultado)
                elif valor < 0:
                    print("El valor ingresado es negativo, no se puede realizar la consignación")
                    break  
            except ValueError:
                print("Debes introducir un número ")
                valor = input("Ingresa el valor a consignar de nuevo: ")

    #Metodo. retirar(double cantidad): se retira una cantidad a la cuenta, si restando la cantidad actual a la que nos pasan es negativa, la cantidad de la cuenta pasa a ser 0 y debe decir cuanto fue lo que pudo retirar
    def retirar(self, valor):
        while(True):
            try: 
                valor = float(valor)
                if self.get_cantidad() < valor:
                    retiro = self.get_cantidad()
                    print("Valor a retirar mayor al saldo, se logro retirar {}.".format(retiro))
                    return self.set_cantidad(0)
                else:
                    resultado = float(self.get_cantidad()) - valor
                    return self.set_cantidad(resultado)

            except ValueError:
                print("Debes introducir un número ")
                valor = input("Ingresa el valor a retirar de nuevo: ")
    
    #Metodo. para mostar el saldo de la cuenta
    def saldo(self):
        print("El saldo de la cuenta es: {} ".format(self.get_cantidad()))
        return self.get_cantidad()

    #Metodo. toString, en python __str__
    def __str__(self):
        return "Cédula: {} \nNombre: {} \nFecha de apertura: {} \nCantidad: {}".format(self.__cedula, self.__nombre, self.__fecha_apertura, self.__cantidad)

    #Realizar un metodo para capturar los datos de nombre, cedula, fecha, cantidad teniendo en cuenta el tipo de dato
    def capturar(self, dato, tipo_dato):
        pass

