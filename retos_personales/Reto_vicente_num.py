#Adivina el numero

#declarando variables
numero_secreto = int(12)

print("Advina cual es el numero secreto")

#haciendo el input del usuario

numero_dado = int(input("adivina el numero: "))
print("\n")
# Bucle con terminacion

while numero_dado != numero_secreto:     
    if numero_dado > numero_secreto:
        print("El numero elegido es incorrecto")
    
        print("PISTA: el número secreto es menor \n")
    elif numero_dado < numero_secreto:
        print("El numero elegido es incorrecto ")
    
        print("PISTA: el número secreto es mayor \n")

    numero_dado = int(input("Vuelvelo a intentar: "))
    print("\n")


print("\n ¡Le achuntaste! \n")

