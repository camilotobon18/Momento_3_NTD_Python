from Cuenta import Cuenta
from Persona import Persona
from Vehiculo import Vehiculo, Coche, Camioneta, Bicicleta, Motocicleta, catalogar

def ejercicio_cuenta():
    print("------Punto 2. Ejercicio Cuenta Bancaria------")
    cedula = input("Ingrese la cédula del titular: ")
    nombre = input("Ingrese el nombre del titular: ")
    fecha_apert = input("Ingrese la fecha de apertura: ")
    cantidad = input("Ingrese la cantidad de dinero de la cuenta (opcional): ")
    cuenta = Cuenta(cedula, nombre, fecha_apert, cantidad)

    while(True):
        try:
            operacion = int(input("Digite el digito de operación a realizar:\n1. Consignar\n2. Retirar\n0. No realizar operación\n"))
            if operacion == 1:
                cuenta.ingresar(input("Ingresa el valor a consignar: "))
                cuenta.saldo()
            elif operacion == 2:
                cuenta.retirar(input("Ingresa el valor a retirar: "))
                cuenta.saldo()
            elif operacion == 0:
                print("Fin de las operaciones")
                break
            else:
                print("Debe intentar con otro número, del 0 al 2")
        except:
            print("Debe ingresar un número del 0 al 2")

    print(cuenta)

def ejercicio_imc():
    nom = input("Digite el nombre: ")
    edad = int(input("Digite la edad: "))
    dni = input("Digite la identificación: ")
    sexo = input("Digite el sexo (H/M): ")
    peso = float(input("Digite el peso(Kg): "))
    altura = float(input("Digite la altura(Mts): "))

    participante = Persona(dni, nombre=nom, edad=edad, sexo=sexo, peso=peso, altura=altura)
    calculo_IMC = participante.calcularIMC()
    mayor_edad = participante.esMayorDeEdad()
    participante.comprobarSexo(sexo)

    if calculo_IMC == -1:
        print("Esta por debajo de su peso ideal")
    elif calculo_IMC == 0:
        print("Esta en su peso ideal")
    elif calculo_IMC == 1:
        print("Tiene sobrepeso")

    #interpretar lo q devuelve la funcion, si es True=mayor_edad, False=menor_edad
    if mayor_edad == True:
        print("Es mayor de edad")
    else:
        print("Es menor de edad")

    print(participante)
    

while(True):
    try:
        punto = int(input("Digite el número del punto a ejecutar:\n1. Ejercicio Contadores\n2. Cuenta bancaria\n3. Ejercicio IMC\n4. Ejercicio Vehiculos\n"))
        if punto == 1:
            pass
            break
        elif punto == 2:
            ejercicio_cuenta()
            break
        elif punto == 3:
            ejercicio_imc()
            break
        elif punto == 4:
            pass
            break
        else:
            print("Valor ingresado no corresponde a uno de los puntos, intenta nuevamente")
    except:
        print("El valor ingresado es incorrecto")


"""
lista_vehiculos = []
auto = Vehiculo('rojo', 4)
escarabajo = Coche('Azul', 4, 250, 1500)
hilux = Camioneta('Negra', 4, 190, 2600, 1500)
montana = Bicicleta('Blanca', 2, "deportiva")
enduro = Motocicleta('Gris', 2, "deportiva", 200, 250)


lista_vehiculos.append(auto)
lista_vehiculos.append(escarabajo)
lista_vehiculos.append(hilux)
lista_vehiculos.append(montana)
lista_vehiculos.append(enduro)

catalogar(lista_vehiculos)
print(lista_vehiculos[0])
"""