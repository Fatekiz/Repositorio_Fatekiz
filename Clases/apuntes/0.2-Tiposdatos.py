#Importando libreria v

import math

print(                                            "####### TIPOS DE DATOS ######## \n") # "\n" --> un "Enter" o un espacio en blanco de separacion de parrafo cuando se imprima

#1.- Números
print("                                  ------- 1.- Números ------- \n               ")
estatura = 1.71 # numero float
peso = 58 # numero int

# potencia (con 2 *) ej: 2**2 --> 2 elevado a 2
imc = peso / (estatura **2)
print(f"1 - {imc}") #Imprimiendo el imc con la operación del elevado 
print(f"1.1 - {math.trunc(imc)}") # Primero llamar libreria (l3) y luego llamar funcion math.trunc(x)

print("                                          ------- 2.- STRINGS         -------\n")

# 2. STRINGS
institucion = "Universidad de Los Lagos" # toda variable "string" que yo asigne debe estar dentro de comillas (" x ") luego del"="
asignatura = "Programación"
descripcion = """Asignatura del primer semestre de la ingieneria 
civil en informatica"""  #Aquí son 3 comillas por lado ya que usamos mas de una linea para la assignacion ("""x""")

#imprimir la posición de un carácter con los corchetes ejemplo print(variable[0] 0 primera letra, 1 segunda y -1 la ultima
print("2 -", institucion[0])
print(f"2.1 - {institucion[1]}") # ocupando el " f- string" encuentro que es la mejor manera para el "print" ej:(print(f "x" {y}) ) 
print(f"2.2 - {institucion[1]}") # y las llaves "{}" son para encapsular y llamar la variable dentro del print(f "y" {x})

#concatenacion
resultado = print("2.3 -", institucion + " " +  asignatura) # la concatenación une las variables con un "+"

# Multiplicando el texto por un número
print("2.4 -",asignatura *4) # multiplicar una variable por un numero es posible, y esto genera una repetición de la variable según la mult.

#División de cadena (split)

print("2.5 -",institucion.split()) # la funcion (x.split) hace que separe cada palabra por separada de la variable

#aplicando len()

print("2.6 -", len(asignatura)) # la funcion ( len(x) ) imprime la cantidad de letras (incluyendo espacios) que contiene la variable "x"

print("                                              ------- 3.- BOOLEANOS -------                        ")

#. 3 BOOLEANOS

ampolleta = False # acá le asignamos a una variable "false" o "true" 
interruptor = True

print(f"3 -{interruptor,ampolleta}") # y acá cuando imnprimamos la variable nos arrojará el valor asignado del bool (si es False/True)

#Salida Booleanas

print(f"3.1 -{1 <= 0 }") # con esto hacemos una pregunta que si lo solicitado está correcto. Esta correcto por ende arroja "False"
print(f"3.2 -{100 > 90}") # nos arrojará un ("True" si es correcto y un "False" si no lo es)
print(f"3.3 -{19 == 19}") # COMENTARIO: "=" --> asignación | "==" --> es de comparación (Matemáticas).
print(f"3.4 -{bool(0)}") # en booleanos existe el true/false 1/0 | este es 0 == false
print(f"3.5 -{bool(1)}") # 1 == True.

print(f"                              ------- impresión de clasificación de variables -------             ")

# impresión de clasificación de variables.
print(f"clas. {type(ampolleta)}") # la función type(x) hace que nos diga a que clase pertenece la variable ej. int, float, bool, str etc...
print(f"clas. {type(asignatura)}")
print(f"clas. {type(peso)}")# COMENTARIO -- la funcion "f -string" la f debe estar pegada al print(f) y pegada al siguiente paréntesis
print(f"clas. {type(imc)}")


print("                                                   ------- LISTAS -------                  ")

# 4.- Listas | Las "listas" son como cajas donde podemos guardar cosas (variables) en ellas, y luego llamarlas o buscarlas cuando las necesitamos  
ciudades = ["Castro", "Queilen", "Ancud", "Quellón", "Chonchi" , "Queilen"]
varios = ["Nicolas", 20, True] 
print(f"clas. {type(ciudades)}") # Acá nos reconoce que la variable "ciudades" es de tipo "list"
print(f"4 - {ciudades}")
print(f"4.1 - {varios}")

#4.1.- forma formal de crear lista "list()" | Nadie la usa xD
lista2 = list(["python", "Ruby"])

print(len(ciudades)) # Cantidad de elementos de una lista 
print(ciudades.count("Queilen")) # Cuenta la cantidad de ocurrencias de un elemento | en este caso "2"

#Impresión de un elemento especifico de una lista
print(ciudades[3])

# Resignando valores de listas 
ciudades[0] = "Quemchi"
print(ciudades) # la posición 0 ya no es castro, es Quemchi

# Funciones de rango con listas
listnum = [ 1, 2, 3 , 4 ,5 , 6, 7, 8, 9, 10]
listnum2 = list(range(10)) #Función de rango | crea una lista con el range() y al colocar cierto valor se crea desde el 0 hasta el valor dado 
listnum3 = list(range(1, 11)) # misma función, solo que usando una "," por separador creamos asi unos limites para que se cree esa lista 


print(listnum2)
print(listnum3)

print("                                      ------- TUPLAS -------              ") # iguales que las listas pero con la diferencia en que son inalterables sus datos dentro de ellas.

musica = tuple()
generos = ("Rock", "POP", "Blues" )

print(generos)
print(type(generos))

print(generos[2]) 

print(generos.index("Rock")) # Consulta la posición de un elemento en específico. 


# Cambio de estructura de tupla a lista. (en este caso es posible cambiar de una tupla a una lista solo usando el list(). ).

tuplita = ("Victor", 200, "Universidad", True)
print(tuplita)
print(f"La tupla  es de tipo {type(tuplita)}")

tuplita = list(tuplita)
print(f"La tupla ahora es de tipo {type(tuplita)}")


print(tuplita[0:3])


print("                     ------        SETS (CONJUNTOS)   ----------      ")

"""     CARACTERISTICAS:

Desordenado: A diferencia de las listas o las tuplas los sets son desordenados, eso significa que no llevan un orden
por lo cual, no es posible consultar su posicion o ocupar un .index() 




"""

# G. SETS (Conjuntos)
conjunto_vacio = set() # Inicializando un set de la forma convencional. (no tan usada)
conjunto_vacio1 ={"JavaScript"} # ??????? (las llaves sirven para Set y dict) (si no hubiera añadido un elemento, lo tomaría como dict)
print(type(conjunto_vacio))
print(type(conjunto_vacio1))


#Iniciaizando sets
colores = {"Azul", "Rojo", "Amarillo", "Verde", "Violeta",}
animales = set({"Gato", "Perro", "Caballo", "Hamster"}) # <-- forma no tan usada... es más rapido solo usar "{}"
print(colores)
print(animales)

# Agregando nuevos elementos al set

colores.add("Negro") #Con la funcion .add() añadi el nuevo elemento "cafe" | al ser los sets desordenados, no se añade al final de la lista.
print(colores)

print("                               --------- DICCIONARIOS ---------------                ")

""" Estructura de datos que permite almacenar sus elementos en pares clave-valor.
    A diferencia de las listas o tuplas que almacenan datos de forma secuencial,
    los diccionarios utilizan el formato clave-valor para acceder a cada elemento y para ocupar funciones usamos las "Claves" 


                 ""Caracteristicas""

    Lista desordenada: no tienen orden en específico.

    Claves unicas: no pueden ser modificadas una vez ya añadidas, y los valores pueden ser cualquier objeto

    Acceso por claves: todos los accesos se hacen por claves en lugar del indice.
"""

paciente = {
    "Nombre" : "alfredo",
        "Edad":29,                           # <-- Forma más usada (Se puede escribir lineal)
        "Ciudad": "Osorno"

}

hospital = dict(
nombre = "Hospital de queilen",
direccion = "Calle jose manuel balmaceda 01",
ciudad = "Queilen"
)

print(paciente)
print(hospital)