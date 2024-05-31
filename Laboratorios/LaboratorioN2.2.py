""" 
Una editorial digital quiere desarrollar una aplicación para gestionar y manipular el contenido de los artículos que publican. 
Es por esto, que se debe crear un módulo que permita realizar diversas operaciones con cadenas de texto para analizar y modificar los
artículos de manera eficiente. (50 Puntos)

Se solicita:

1. Ingresar un breve resumen del artículo igual o menor a 60 caracteres. Solicitar este breve resumen por terminal.

2. Crear una variable booleana que almacene True si la longitud de la variable que almacena el resumen es igual o menor a 60 caracteres y False en caso contrario.

3. Mostrar en pantalla las siguientes operaciones:

a. Imprimir la longitud de caracteres del breve resumen del artículo.

b. Convertir el resumen en mayúsculas utilizando la función de Python
adecuada.

c. Mostrar los últimos diez caracteres del resumen.

d. Unir las palabras del resumen con un guión (-) como separador utilizando la
función correcta.


"""

# Descripción para usar: Hola amigo victor como estas 

"""                                               1                              """
print("\n ")
# --- pedir resumen igual o menor a 60 carácteres --- (1)
articulo = str(input("ingrese una breve descripción del articulo (debe ser igual o menor de 60 carácteres): "))
print("\n")

while len(articulo) >= 60:
    print(" Su descripcion contiene más de 60 carácteres, inténtelo denuevo.")
    articulo = str(input("ingrese una breve descripción del articulo (debe ser igual o menor de 60 carácteres): "))


else:
     print(f"la descripcion agregada es: {articulo} \n")


"""                                             2                             """

# --- crear variable booleana --- (2)

verdadero = len(articulo) <= 60 


"""                                             3                            """

# Imprimir la longitud de carácteres del breve resumen (a)

print(f"La longitud de carácteres de la descripcion es de: {len(articulo)} caracteres \n") 

# Convertir el resumen a Mayúsculas (b)
print(f"El resumen transformado a mayusculas sería: {articulo.upper()} \n")

# mostrar los ultimos 10 caracteres del resumen. (c)

print(f"Los ultimos 10 carácteres de la descripción es:{articulo[-10 :]}")

# unir las palabras del resumen con un guión (-) como separador. 
newarticulo = articulo.split()

print("-" .join(newarticulo))