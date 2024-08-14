# Realizar un algoritmo que permita obtener el resultado de la expresión n**n con datos ingresados por consola

print("\n Bienvenido usuario, ingrese un numero y sera multiplicado por si mismo \n")

while True:
    numero = int(input("Ingrese el numero: \n"))
    print(f"El numero ingresado fue: {numero} \n" )

    resultado = (numero **numero)
    print(f"{numero} elevado a {numero}, es igual a: {resultado} \n")
    respuesta = input("¿desea intentarlo nuevamente? (S/N)")
    
    if respuesta == "n" or respuesta == "N":
        print("Proceso terminado")
        break
    else:
        print("OK! aquí vamos denuevo \n")
    

# TERMINADO !!