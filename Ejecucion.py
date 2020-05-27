from Persona import Persona

def ejercicio_imc():
    nom = input("Digite el nombre: ")
    edad = int(input("Digite la edad: "))
    dni = input("Digite la identificación: ")
    sexo = input("Digite el sexo (H/M): ")
    peso = float(input("Digite el peso: "))
    altura = float(input("Digite la altura: "))

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

ejercicio_imc()