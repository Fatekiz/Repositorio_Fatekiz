# Crear un programa que pida al usuario las medidas de ambos catetos de un triángulo para determinar la hipotenusa
# si se ingresa un numero igual o menor a 0 entonces se repite el programa

def calculahipotenusa():

    print("Bienvenido usuario. Ingrese las medidas de 2 catetos de un triangulo para imprimir la medida de la hipotenusa")

    while True:
        cateto_1 = int(input("Ingrese medida de cateto 'a': "))

        if cateto_1 > 0:
            print(f"Medida del cateto 'a': {cateto_1} ")
            while True:
                cateto_2 = int(input("Ingrese medida de cateto 'b': "))

                if cateto_2 > 0:
                    print(f"Medida del cateto 'b': {cateto_2} ")

                    h = (cateto_1 **2) + (cateto_2 **2)
                    print(f"El resultado es: Raíz cuadrada de: {h}")
                    break
                else:
                    print("Medida incorrecta. Intente denuevo (debe ser mayor a 0) \n")    
            break    
        else:
            print("Medida incorrecta. Intente denuevo (debe ser mayor a 0) \n")

calculahipotenusa()

# TERMINADO!