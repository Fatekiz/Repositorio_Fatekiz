"""
determinar el factorial de un número
"""

factorial = int(input("Ingrese el número del cual desee obtener su factorial (x!) "))

resta =  (factorial - 1) # con esto sacaré el factorial de cada número.

numeros = []

resultado_f = 1

if factorial == 0: # si el numero dado es 0 se imprimira el numero 1
    print("factorial de 0 es: 1")
else: # de lo contrario:
    print(f"factorial de '{factorial}' ")
    while factorial != 0: # mientras factorial sea distinto a 0:
        numeros.append(factorial) # sumando factorial
        factorial -= 1 # cambiando factorial restandole 1
    for i in numeros:
        resultado_f *= i
    print(f"                es: {resultado_f} ")

# Terminado