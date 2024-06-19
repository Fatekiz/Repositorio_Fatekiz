import numpy as np

#                                                       FUNCIONES

# Funciones:

"""
Bloque de código reutilizables que realiza algo en específico

para que funcione se debe llamar:

caracteristicas:
argumentos: deben pasarse a la funcion
Invocada: se debe llamar por su nombre para imprimir ese código en especifico
ambitos de variables: Las variables definidas dentro de una funcion tienen un ámbito local, osea son accesibles dentro de la función
"""
#Ejemplo de crear una funcion


def saludo(): #<--- al crear una funcion debo ser especifico según lo que hace
    print("Hola mi nombre es benjamin")


saludo() # <--- aquí la estoy llamando, no debe tener indentación

# creando funcion matemática

def funcion(x):
    return x + 10

y = funcion(10)
print(y)


def saludo(name): # <-- "name" es mi "x"
    print(f"Hola mi nombre es {name}") # <-- ocupo la variable "name" que se remplazará para luego ser remplazada abajo.


saludo("Orlando") 

#    LA IDEA DE USAR FUNCIONES ES REUTILIZAR CÓDIGOS Y ASÍ SIMPLIFICAR NUESTROS CÓDIGOS




#         BIBLOTECA, LIBRERIA , PAQUETES
# funciones especificas que no estan de forma nativa en el lenguaje que sirven para simplificar.

# bibloteca | NUMPY | ofrece:
#sirve para trabajar con BIG DATA, 

# bibloteca | pandas | ofrece: sirve muchop para analisis de datos
# cargar datos, modelar datos ,analizar datos

# bibloteca | random | ofrece:  sirve muchop para analisis de datos
# sirve para dar datos al azar