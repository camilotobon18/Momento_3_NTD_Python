class Vehiculo():

    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "Color {}. {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindraje):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje
    
    def __str__(self):
        return 'color {}, {} Km/h, {} ruedas, {} cc'.format(self.color, self.velocidad, self.ruedas, self.cilindraje)

class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindraje, carga):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindraje = cilindraje
        self.carga = carga

    def __str__(self):
        return 'color {}, {} km/h, {} ruedas, {} cc, {} Kg de carga'.format(self.color, self.ruedas, self.velocidad, self.cilindraje, self.carga)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo

    def __str__(self):
        return 'color {}, {} ruedas, tipo {}'.format(self.color, self.ruedas, self.tipo)

class Motocicleta(Bicicleta):
    def __init__(self, color, ruedas, tipo, velocidad, cilindraje):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo
        self. velocidad = velocidad
        self.cilindraje = cilindraje

    def __str__(self):
        return 'color {}, {} ruedas, tipo {}, {} km/h, cilindraje {}'.format(self.color, self.ruedas, self.tipo, self.velocidad, self.cilindraje)



def catalogar(lista_vehiculos):
    c_cuatro_ruedas = 0
    lista_cuatro_ruedas = []
    lista_cuatro_ruedas.append([])
    #lista_cuatro_ruedas.append([])
    for vehiculo in lista_vehiculos:
        if vehiculo.ruedas == 4:
            c_cuatro_ruedas = c_cuatro_ruedas + 1
            lista_cuatro_ruedas[0].append(vehiculo)
            #lista_cuatro_ruedas[1].append(vehiculo.ruedas)
    
    print("Se han encontrado {} vehiculos con 4 ruedas".format(c_cuatro_ruedas))
    for vehi_cuatro in lista_cuatro_ruedas:
        print(str(  vehi_cuatro))
    
    return c_cuatro_ruedas, lista_cuatro_ruedas

