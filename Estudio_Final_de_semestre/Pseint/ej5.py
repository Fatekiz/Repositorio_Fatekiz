# crear un programa que al ingresar un numero oingrese mas opciones para calclar el area y el perimtetro de la figura seleccionada

def calcular_perimetro():

    print("Bienvenido usuario a continuacion ingrese un numero")
    print("Cada numero esta asociado a una figura geometrica")
    print("Los cuales son: \n")
    print(" 1.- cuadrado")
    print(" 2.- Triángulo")
    print(" 3.- circulo")

    while True:

        opcion = input("Ingrese la opcion de la figura que desee obtener los cálculos: ")

        if opcion == '1':
            print("cuadrado")
            lado = int(input("Ingrese el lado del cuadrado: "))
            area = lado * lado
            perimetro = lado *4
            print(f"El Área es: {area}")
            print(f"El Perímetro es: {perimetro}")
            break

        elif opcion == '2':
            print("Triángulo")
            h = int(input("Ingrese la altura del Triángulo: "))
            lado1 = int(input("Ingrese el lado 1: "))
            lado2 = int(input("Ingrese el lado 2: "))
            base = int(input("Ingrese la base: "))
            area = (base * h) /2
            perimetro = lado1 + lado2 + base
            print(f"El Área es: {area}")
            print(f"El Perímetro es: {perimetro}")
            break

        
        elif opcion == '3':
            print("Círculo")
            radio = int(input("Ingrese el radio: "))
            area = 3.1416 *radio *radio
            perimetro = (2*3.1416) * radio
            print(f"El Área es: {area}")
            print(f"El Perímetro es: {perimetro}")
            break

        else:
             print("Opción errónea, por favor seleccione una opción válida (1, 2, o 3). \n")

calcular_perimetro()

# TERMINADO!