""" Crear algoritmo que genere las series de fibonacci basadas en valor n ingresado por teclado solo usando bucles"""

n = int(input("Ingrese el numero tope hasta donde llegue la serie de fibonacci "))
a = 0
b = 1

lista = [a,b]

while True:
    c = a + b
    if c > n:
        break
    lista.append(c) 
    a = b
    b = c
    # a, b = b, c <-- permutacion, resumo lo de arriba en una sola linea.

print(" ".join(map(str,lista)))