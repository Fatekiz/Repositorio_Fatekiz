####Crear 20 numeros, que se encuentren en el intervarlo 40 al 350 y los almacene en una 
##lista y luego pida buscar algun numero dentro de los almacenados. Adem ´ as que muestre 
###la cantidad de ocurrencias de ese numero buscado. (Se permite el uso de la Biblioteca Random)
import random

# generando 20 numeros entre el 40 y el 350
numeros = [random.randint(40, 350) for i in range(20)] ###randint es la funcion de la biblioteca random para buscar numeros aletatorios en rango especifico

# imprimiendo los numeros
print("Numeros aleatorios:", numeros)
numero_buscar = int(input("Ingrese un número para buscar en la lista: "))

#cuantas veces aparece el numero
cantidad = numeros.count(numero_buscar)

# imprimiendo cantidad de veces 
print(f"El numero {numero_buscar} aparece {cantidad} vez/veces en la lista.")

# Terminado.