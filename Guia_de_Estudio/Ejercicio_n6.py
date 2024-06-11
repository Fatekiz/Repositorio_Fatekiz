"""

6. Una empresa de Marketing Digital necesita crear un programa donde se puedan seleccionar
automáticamente 5 palabras claves para un sitio web. Estas palabras claves se deben
almacenar en una lista. Se solicita realizar las siguientes operaciones:

a. Ingresar 5 palabras por terminal y almacenarlas en una lista.

b. Eliminar las palabras duplicadas utilizando una estructura.

c. Mostrar la lista original y la estructura resultante.


"""

p1 = input("Ingrese la primera palabra: ")
p2 = input("Ingrese la segunda palabra: ")
p3 = input("Ingrese la tercera palabra: ")
p4 = input("Ingrese la cuarta palabra: ")
p5 = input("Ingrese la quinta palabra: ")


palabras_claves = [p1,p2,p3,p4,p5]

print(palabras_claves)

print(f"Lista sin las palabras repetidas: \n")

palabras_no_rep = set(palabras_claves)

print(palabras_no_rep)