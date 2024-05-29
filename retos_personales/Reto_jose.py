# Ingese 5 numeros por consola y coloquelos en una lista de menor a mayor
numeros = []
print("Ingrese 5 numeros ")

n1 = int(input("Ingrese el primer numero: "))
n2 = int(input("Ingrese el primer numero: "))
n3 = int(input("Ingrese el primer numero: "))
n4 = int(input("Ingrese el primer numero: "))
n5 = int(input("Ingrese el primer numero: "))

numeros = [n1,n2,n3,n4,n5]
orden = []

nn1 = min(n1,n2,n3,n4,n5)
numeros.remove(nn1)
orden = []
orden.append(nn1)

nn2 = min(numeros)
orden.append(nn2)
numeros.remove(nn2)

nn3 = min(numeros)
orden.append(nn3)
numeros.remove(nn3)

nn4 = min(numeros)
orden.append(nn4)
numeros.remove(nn4)

nn5 = min(numeros)
orden.append(nn5)

print(orden)