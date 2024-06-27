"""Resolver el ejercicio propuesto a continuación. Se solicita desarrollar la solución utilizando Python.
No se puede utilizar apuntes, o código anteriores. Tiempo para resolver el ejercicio: 45 minutos.
"""

"""1. Se cuenta con tres tuplas: la primera contiene las alturas de los volcanes más altos en la
Zona Central. La segunda tupla contiene las alturas de los volcanes más altos en la Zona Sur.
Por último, en la tercera tupla las alturas de volcanes de la Zona Austral.

● Alturas en Zona Central: {8848, 8611, 8586, 8200, 8460, 8200}

● Alturas en Zona Sur: {8848, 5567, 8125, 4560, 8051, 4560}

● Alturas en Zona Austral: {2200, 2500, 1000, 2200, 3623, 990}

A) Imprimir los valores duplicados de cada tupla

B) Verificar si la altura 8848m se encuentra en las tres tuplas con la función
correspondiente en Python.

C) Unir las tuplas en una sola y eliminar los duplicados.

D) Transformar la tupla obtenida en una lista. Imprimir la nueva lista obtenida.
"""
#Ingresando las tuplas
alturas_central = (8848,8611,8586,8200,8460,8200)
alturas_sur = (8848, 5567, 8125, 4560, 8051, 4560)
alturas_austral = (2200, 2500, 1000, 2200, 3623, 990)

# A)con "for"

for zona, altura in zip()