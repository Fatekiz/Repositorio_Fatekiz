"""
Se necesita desarrollar un código que permita ingresar una descripción breve de un artículo
de librería. Por ejemplo: “Este lápiz solo tiene formato de color azul”. Se solicita realizar las
siguientes operaciones:

no tener mas de 50 carcteres
que imprima si es verdadero q tiene menos de 50
imprimir las primeras 10 palabras
"""
lapiz = "Solo hay 2 colores de lápices, rojo y azul"

f = (len(lapiz) <= 50)
print(f)
print(type(f))

print(lapiz[ :10])
