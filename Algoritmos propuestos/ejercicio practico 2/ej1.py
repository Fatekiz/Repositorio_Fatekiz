"""
Se cuenta con tres tuplas: la primera contiene los puntajes más altos obtenidos por
estudiantes en Matemáticas. La segunda tupla contiene los puntajes más altos en Química.
Por último, la tercera tupla contiene los puntajes más altos en Programación.

A) Imprimir los valores duplicados de cada tupla
B) Convertir cada tupla en una lista y ordenar las listas en orden descendente.
C) Unir las listas anteriormente generadas en una sola y eliminar los duplicados.
D) Encontrar el puntaje máximo y mínimo de la lista resultante.

"""

# Puntajes mas altos de cada asignatura
matematicas = (55, 17, 93, 75, 88, 55) # 55 duplicado
quimica = (10, 85, 75, 88, 91, 75) # 75 duplicado
programacion = (68, 78, 85, 68, 82, 10) # 68 duplicado
duplicados = []

# funcion: 
def fun_duplicar(x):
    contador = 0
    for i in x:
        if x.count(i)>1:
            contador +=1
            if contador > 1:
                if i not in duplicados:
                    duplicados.append(i)
                    contador = 0
                    return duplicados
                
               

# A) Imprimir los valores duplicados de cada tupla
fun_duplicar(matematicas)
fun_duplicar(quimica)
print(fun_duplicar(programacion))

# ---listo---

# ------------------------------------------

desc_mates = []
desc_quimica = []
desc_progra = []

# funcion:
def descendente(y): # "y" sera el nombre de la variable de cada lista | # "o" sera el nombre para las nuevas listas

    global desc_mates # el global es para acceder a variables (globales) (que ya esten registradas antes)
    while y: 
        num_alto = max(y)
        desc_mates.append(num_alto)
        y.remove(num_alto)

    return desc_mates

def descendente2(o): # "y" sera el nombre de la variable de cada lista | # "o" sera el nombre para las nuevas listas

    global desc_quimica # el global es para acceder a variables (globales) (que ya esten registradas antes)
    while o: 
        num_alto = max(o)
        desc_quimica.append(num_alto)
        o.remove(num_alto)
    return desc_quimica

def descendente3(q): # "y" sera el nombre de la variable de cada lista | # "o" sera el nombre para las nuevas listas

    global desc_progra # el global es para acceder a variables (globales) (que ya esten registradas antes)
    while q: 
        num_alto = max(q)
        desc_progra.append(num_alto)
        q.remove(num_alto)
    return desc_progra


# B) Convertir cada tupla en una lista y ordenar las listas en orden descendente.

mates_lista = list(matematicas)
quimica_lista = list(quimica)
progra_lista = list(programacion)

mate_desc = descendente(mates_lista)
quimica_desc = descendente2(quimica_lista)
progra_desc = descendente3(progra_lista)

print(f"\n Listas ordenadas de forma descendentes: \n \n 1.- {mate_desc} \n 2.- {quimica_desc} \n 3.- {progra_desc} \n ")

# ---Listo---

# --------------------------------------------

# C) Unir las listas anteriormente generadas en una sola y eliminar los duplicados.

listas_unidas = mate_desc + quimica_desc + progra_desc 
print(f"las listas unidas: {listas_unidas}")

notas_unicas = []

for i in listas_unidas:
    if listas_unidas.count(i)<2 or i not in notas_unicas:
        notas_unicas.append(i)

print(f"Lista de todas las notas sin repeticiones: {notas_unicas}\n ")

# ---listo---

# -----------------------------------------------

# D) Encontrar el puntaje máximo y mínimo de la lista resultante.

print(f"El puntaje máximo de la lista anterior es: {max(notas_unicas)} \n y el minimo es: {min(notas_unicas)}")

# ---Listo---