# crear programa que cuente el numero de digitos en un numero entero positivo   

numero = int(input("ingrese un numero entero positivo y el programa imprimirá el total de digitos: "))
contador = 0

while numero > 0:
    numero //= 10
    contador +=1
print(f"El total de digitos es de: {contador}.")