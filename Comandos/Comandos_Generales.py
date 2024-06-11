"""                                                  ----- COMANDOS QUE HE APRENDIDO -------                                      """

#VARIABLES PARA USAR 

x = "variable"
y = 123.456
nombre = "benjamin"
nombre_completo = "Benjamin Concha"


#                        2. TRANSFORMAR A UN TIPO DE DATO
int() # num entero
float() # num flotante
complex() # num complejo
str() # string o cadena
bool() # booleano (0,1)


#                         1. IMPRIMIR """Con prueba """
print("prueba") # <-- Funciona para imprimir el mensaje que yo quiera en la consola, este debe estar seguido de ("con el mensaje")
print(f"prueba, {x}") # <-- Personalmente prefiero usar el f-string ya que para mi me es más comodo si debo usar una variable usando "{}"

#                            INPUT

input() # <-- Con esto podemos solicitar un dato al usuario, el cual lo debe escribir en la consola 

""" Prueba """

variable_segun_input = input("ingresa un dato") # <-- Con esto inmediatamente la variable tomará el valor ingresado por consola
# print(f"Llamar variable {Variable_segun_input}")


#                                OPERACIONES MATEMATICAS
round # redondea un numero 

""" Prueba """
round(y,2) # Redondea a num. entero la variable que yo encierre en () despues del round según la cantidad de decimales que yo eliga despues de la ","

#                                      SECUENCIAS

list # <-- crea lista
tuple # <-- crea tuplas
range # <-- crea rangos

""" Prueba """

lista_de_num = [1,2,3]
Ciudades = ["Queilen" , "Castro", "Queilen", "Santiago"]
Ciudades_Santiago = ["Puente alto", "La Florida"]
Rango_numerico = list(range(0,11)) # <-- asi tendra 10 numeros dentro (cuenta desde el 0) por ende si quiero llegar hasta 10 debo usar el "(x,11)".

#                                   OPERACIONES 

len # imprime la cantidad de elementos o carácteres
min # imprime el valor minimo
max # imprime el valor máximo
x.split # <-- Me separa las cadenas de una variable
x.upper # me convierte una cadena de texto a todo en MAYUSCULAS pero debo guardarlo en una nueva variable
x.lower # me convierte una cadena de texto a todo en minusculas pero debo guardarlo en una nueva variable
x.index # imprime la posición del elemento a consultar
x.count # cuenta la cantidad de ocurrencias de un elemento dentro de una lista
"" .join # <-- Me permite agregar lo que yo agregue dentro del " " entre cada elemento de la lista
Ciudades.append # <-- Agrega el elemento que coloque en () despues de append a la lista
Ciudades_Santiago.clear # <-- Elimina todos los elementos de esas lista
Ciudades.remove # <-- Elimina el elemento que coloque dentro de () despues de remove , si hay repetidos solo elimina el primero.
Ciudades.reverse # <-- Invierte los datos de la lista, todo al revéz 
x.capitalize # <-- Convierte el primer caracter en mayusculas, los demas en minusculas
x.casefold # <-- Convierte todo a minusculas, es parecido al x.lower()

""" Prueba """
print(len(Rango_numerico)) # contiene 10 numeros (del 0 al 10)

print(len(Ciudades)) # contiene 4 elementos (ciudades)

print(min(Rango_numerico)) # Numero más pequeño del elemento Rango_numerico (0)

print(max(Rango_numerico)) # Numero mas grande del elemento Rango_numerico (10)

print(Ciudades.index("Santiago")) # santiago es el numero 3, ya que se cuenta desde el 0 | Queilen = 0 , Castro = 2

print(Ciudades.count("Queilen")) # arroja 2, ya que esta "2" veces repetida

CiudadesConEspacio = " " .join(Ciudades) # Estoy agregando espacio entre cada elemento con el " "
print(CiudadesConEspacio)

Ciudades.append("Los Chonos") # Agrego "Los Chonos" Al final de la lista
print(Ciudades)

Ciudades_Santiago.clear() # Me eliminó todos los elementos de esa lista
print(Ciudades_Santiago)

Ciudades.remove("Queilen") # Me elimino el primer queilen que habia repetido
print(Ciudades)

Ciudades.reverse() # Inviritió el orden de los elementos dentro de ciudades.
print(Ciudades) 

NombreF = nombre.capitalize() # Convierte el primer caracter en mayuscula
print(NombreF)

nombreN = NombreF.casefold() # Convierte todo a minusculas
print(nombreN)

nombreM = nombre.upper() # Convirtió la cadena entera a mayuscula
print(nombreM)

nombrem = nombre.lower() # Convirtió la cadena entera a minuscula
print(nombrem)

print(nombre_completo.split()) # Separo la cadena de la variable por " , "


#                               BUCLES

while x == x: 

    break

if x == x:
    x = 10

#                         Listas

# append() <--- agrega un elemento al final de la lista
# insert() <--- inserta un elemento en un lugar específico de la lista
# extend() <--- combina 2 o más listas
# remove() <--- elimina la primera ocurrencia de un elemento (en caso de que este duplicado)
# pop() <--- Borra y retorna el último elemento de una lista
# sort() <--- ordena los elementos de la lista de manera ascendete



#                              TUPLAS (tuple)

# count() <--- imprime el total de repeticiones que tiene el elemento seleccionado dentro de la tupla
# index() <--- imprime el indice con el elemento seleccionado en la tupla
# sorted() <--- Entrega una lista ordenada con los valores de la tupla
# min() <--- devuelve el valor minimo de la tupla
# max() <--- devuelve el valor máximo de la tupla
# sum() <--- imprime la suma de los valores dentro de la tupla





#                             SETS

# add() <- añade elementos al set seleccionado
# clear() <- elimina todos los elementos del set
# discard () <--- elimina un elemento del set
# copy() <- crea una copia del set 
# intersection() <--- devuelve un solo set que contiene solo los valores que esetan en ambos sets
# difference() <--- a diferencia del intersection devuelve un set que contiene los elementos que estan en el set 1 pero no en el 2
# pop() <--- eliminar un archivo del set
# remove() <--- eliminar la primeria ocurrencia de un elemento dentro del set
# len() <--- cuenta cantidad de elementos dentro del set


#                   DICCIONARIOS

# keys() <--- devuelve lista con todas las claves del diccionario
# values() <--- devuelve una lista con todos los valores del diccionario
# items() <--- devuelve una lista de tuplas donde cada tupla contiene una clave junto con su valor
# clear() <--- limpia la lista
# copy() <--- hace una copia del diccionario
# pop() <-- elimina la clave y valor (llamando la clave)

#             ---- Listas ----
# sort() <-- Lo ordena 