import random
from Cuenta import Cuenta
from Persona import Persona
from Contador import Contador
from Vehiculo import Vehiculo, Coche, Camioneta, Bicicleta, Motocicleta, catalogar

def ejercicio_contador():
    inicial = Persona.validacion_dato(input("Digite el número por el que quiere empezar (por defecto es 0): "), int)
    frecuencia = Persona.validacion_dato(input("Digite la frecuencia 1, 2, 3...(por defecto es 1): "), int)
    contar = Contador(inicial, frecuencia)
    validacion = True
    while(validacion):
        accion = Persona.validacion_dato(input("Digite 1 para incrementar, 2 para decrementar, 0 para salir: "), int)
        if accion==1:
            contar.incrementar()
        elif accion==2:
            contar.decrementar()
        else:
            validacion = False

def ejercicio_cuenta():
    print("------Punto 2. Ejercicio Cuenta Bancaria------")
    cedula = input("Ingrese la cédula del titular: ")
    nombre = input("Ingrese el nombre del titular: ")
    fecha_apert = input("Ingrese la fecha de apertura: ")
    cantidad = input("Ingrese la cantidad de dinero de la cuenta (opcional): ")
    cuenta = Cuenta(cedula, nombre, fecha_apert, cantidad)

    while(True):
        try:
            operacion = int(input("Digite el digito de operación a realizar:\n1. Consignar\n2. Retirar\n3. Ver Saldo\n0. No realizar operación\n"))
            if operacion == 1:
                cuenta.ingresar(input("Ingresa el valor a consignar: "))
                cuenta.saldo()
            elif operacion == 2:
                cuenta.retirar(input("Ingresa el valor a retirar: "))
                cuenta.saldo()
            elif operacion == 3:
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
    edad = Persona.validacion_dato(input("Digite la edad: "), int)
    dni = input("Digite la identificación: ")
    sexo = input("Digite el sexo (H/M): ")
    peso = Persona.validacion_dato(input("Digite el peso(Kg): "), float)
    altura = Persona.validacion_dato(input("Digite la altura(Mts): "), float)

    participante = Persona(dni, nombre=nom, edad=edad, sexo=sexo, peso=peso, altura=altura)
    calculo_IMC = participante.calcularIMC()
    mayor_edad = participante.esMayorDeEdad()
    participante.comprobarSexo(sexo)
    DNI_aleatorio = participante.generar_DNI()

    print("Su DNI generado aleatoriamente es {}".format(DNI_aleatorio))
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
    
def ejercicio_vehiculos():
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

    c_cuatro_ruedas, listado = catalogar(lista_vehiculos)
    print("Se han encontrado {} vehiculos con 4 ruedas".format(c_cuatro_ruedas))
    for vehiculo in listado:
        print(vehiculo)

while(True):
    try:
        punto = int(input("Digite el número del punto a ejecutar:\n1. Ejercicio Contadores\n2. Cuenta bancaria\n3. Ejercicio IMC\n4. Ejercicio Vehiculos\n"))
        if punto == 1:
            ejercicio_contador()
            break
        elif punto == 2:
            ejercicio_cuenta()
            break
        elif punto == 3:
            ejercicio_imc()
            break
        elif punto == 4:
            ejercicio_vehiculos()
            break
        else:
            print("Valor ingresado no corresponde a uno de los puntos, intenta nuevamente")
    except:
        print("El valor ingresado es incorrecto")



