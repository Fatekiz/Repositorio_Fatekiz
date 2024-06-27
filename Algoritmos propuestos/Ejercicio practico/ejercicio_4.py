"""Crea un algoritmo que permita adivinar un número.
En primer lugar el algoritmo debe solicitar un número entero por consola. 
A continuación va pidiendo números y va respondiendo si el número a adivinar es mayor o menor que el introducido. 
El programa termina cuando se acierta el número."""

# numero secreto.

num_secreto = int(input("Bienvenido usuario ingrese un número secreto para que acontinuación lo adivine: "))

#iniciando programa 

print(" ¡Adivine el numero secreto!")

adivinar = int(input("Adivine el numero: "))

while adivinar != num_secreto:

    if adivinar > num_secreto:
        adivinar = int(input("\n--- ¡Te equivocaste! --- (aquí va una pista: el numero secreto es menor) \n Adivine nuevamente el numero: "))
    else:
        adivinar = int(input("\n--- ¡Te equivocaste! --- (aquí va una pista: el numero secreto es mayor) \n Adivine nuevamente el numero: "))
print("\n --- ¡FELICIDADES ADIVINASTE! --- \n ")