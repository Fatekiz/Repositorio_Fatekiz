"""1. Obtener la cantidad de veces que se repite la palabra “universidad” dentro del siguiente
parrafo: 
“La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional 
entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus 
pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participación
democratica.” 
Guardar las palabras encontradas dentro de una tupla
"""

enunciado = "La Universidad de los Lagos es una institucion estatal fundada en 1993. Esta universidad regional entrega una contribucion significativa al desarrollo sostenible del territorio. Como Universidad sus pilares fundamentales se basan en la inclusion, pluralismo, conciencia ambiental y participación democratica."

enunciado_split = enunciado.split()
print(enunciado_split)

tupla = ("la palabra se repite: ", enunciado_split.count("universidad"), "vez")
print(tupla)
print(type(tupla)) #me aseguro que esta en una tupla