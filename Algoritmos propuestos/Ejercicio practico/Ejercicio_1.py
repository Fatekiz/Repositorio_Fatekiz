"""Resolver el ejercicio propuesto a continuación. Se solicita desarrollar la solución utilizando Python.
No se puede utilizar apuntes, o código anteriores. Tiempo para resolver el ejercicio: 45 minutos.
"""

"""1. Se cuenta con tres tuplas: la primera contiene las alturas de los volcanes más altos en la
Zona Central. La segunda tupla contiene las alturas de los volcanes más altos en la Zona Sur.
Por último, en la tercera tupla las alturas de volcanes de la Zona Austral.

● Alturas en Zona Central: {8848, 8611, 8586, 8200, 8460, 8200}

● Alturas en Zona Sur: {8848, 5567, 8125, 4560, 8051, 4560}

● Alturas en Zona Austral: {2200, 2500, 1000, 2200, 3623, 990}

A) Imprimir los valores duplicados de cada tupla (listo)

B) Verificar si la altura 8848m se encuentra en las tres tuplas con la función
correspondiente en Python.

C) Unir las tuplas en una sola y eliminar los duplicados.

D) Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida.
"""
#Ingresando las tuplas
alturas_central = (8848,8611,8586,8200,8460,8200) # 8200
alturas_sur = (8848, 5567, 8125, 4560, 8051, 4560) # 4560
alturas_austral = (2200, 2500, 1000, 2200, 3623, 990) # 2200
contador = 0
duplicados = []

# A)con "for"

for altura in alturas_central:
    if alturas_central.count(altura) > 1:
        contador+=1
        if contador>1:
            if altura not in duplicados:
                duplicados.append(altura)
                contador = 0


for altura2 in alturas_sur:
    if alturas_sur.count(altura2) > 1:
        contador +=1
        if contador > 1:
            if altura2 not in duplicados:
                duplicados.append(altura2)
                contador = 0


for altura3 in alturas_austral:
    if alturas_austral.count(altura3)>1:
        contador+=1
        if contador > 1:
            if altura3 not in duplicados:
                duplicados.append(altura3)

print(duplicados)
#(---listo---)


# B)  Verificar si la altura 8848m se encuentra en las tres tuplas con la función correspondiente en Python.

if 8848 in alturas_central and 8848 in alturas_sur and 8848 in alturas_austral:
    print("La altura '8848' se encuentra en las 3 tuplas. \n")
else:
    print("La altura '8848' no se encuentra en las 3 tuplas. \n")
# (---Listo---)

# C) Unir las tuplas en una sola y eliminar los duplicados.

tuplas = alturas_central + alturas_sur + alturas_sur
tuplas_set = set(tuplas)
new_tuplas = tuple(tuplas_set)
print(new_tuplas)
# (---listo---)

#D) Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida.

print(f"Tupla anterior transformada a lista: {list(new_tuplas)}")

# TERMINADO!