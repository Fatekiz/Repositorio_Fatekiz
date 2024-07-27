# sumar numeros hasta que un usuario ingrese un 0
suma = 0
num_base = int(input("Ingrese un numero del 1-9 para irlos sumando repetitivamente hasta que ingerese un 0: "))

while num_base != 0:
    suma += num_base
    print(f"La suma total va siendo: {suma}")
    num_base = int(input("Ingrese un numero del 1-9 para que se vayan sumando repetitivamente hasta que ingerese un 0: "))
print(f"La suma total fue: {suma}")