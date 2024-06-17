""" Crear algoritmo que genere las series de fibonacci basadas en valor n ingresado por teclado solo usando bucles"""

n = int(input("Ingrese el numero tope hasta donde llegue la serie de fibonacci "))
a = 0
b = 1

lista = []

while a < n:
    print(a)
    a = a + b
    f = (a) + (a-1)
    lista.append(f)
    print(lista)


"""
Plasmar para entender: 

    0 , 1 , 1 , 2 , 3 ,5 , 8 , 13 , 21 , 35 

    a + b

    a = 0
    b = 1




"""