"""
Desarrollar un código que permita ingresar 3 ciudades con sus respectivas latitud y longitud
(x, y) en números flotantes. Guardar las ciudades en una lista y las coordenadas en tuplas.
Mostrar la siguiente información:


a. Crear el nombre de 3 ciudades y sus respectivas coordenadas (x, y) mediante código
en números flotantes.
b. Almacenar las ciudades en una lista y las coordenadas en tuplas.
c. Mostrar el nombre de cada ciudad junto con sus coordenadas.
d. Obtener solo la parte entera de las coordenadas de cada ciudad utilizando una
función propia de Python

"""
import math

# A) Creando el nomvre de las 3 ciudades
ciudad1 = "queilen"
ciudad2 = "castro"
ciudad3 = "chonchi"

cor1 = 7.7
cor2 = 6.5
cor3 = 4.3

# B) almacenando ciudades (lista) coordenada (tupla)

name_ciudades = [ciudad1,ciudad2,ciudad3]
cor_ciudades = (cor1,cor2,cor3)

# C) Mostrar el nombre de la ciudad junto con sus coordenadas

print(f"Ciudad 1: {ciudad1}, tiene las coordenadas: {cor1}")
print(f"Ciudad 2: {ciudad2}, tiene las coordenadas: {cor2}")
print(f"Ciudad 3: {ciudad3}, tiene las coordenadas: {cor3}")


# D) obtener solo la parte entera de las coordenadas de cada ciudad utilizando una funcion propia de python.

print(f"latitud de {ciudad1}: {math.trunc(cor1)} ") # <--- para esto me fue necesario llamar la libreria "math" (import math)
print(f"latitud de {ciudad2}: {math.trunc(cor2)} ")
print(f"latitud de {ciudad3}: {math.trunc(cor3)} ") 


#                       TERMINADO.