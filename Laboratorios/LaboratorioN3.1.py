""" A) Guardar la información de la Tabla N°1 en un diccionario llamado censo_2017.
Dentro de este diccionario estarán otros dos diccionarios
donde las claves serán el ID Región (14 y 12).
 Los valores asociados a estas claves serán diccionarios que contengan el Nombre Región, Superficie y Habitantes. 
Luego, imprimir el diccionario obtenido """

superficie1 = 18429
habitantes1 = 404432

superficie2 = 1382291
habitantes2 = 166533


censo_2017 = {

    "id region1": { 14 : {    "nombre region" : "los rios" , "superficie" : {superficie1} , "habitantes" : {habitantes1} } } , # <- mal key
    "id region2": { 12 :  {    "nombre region" : "magallanes" , "superficie" : {superficie2} , "habitantes" : {habitantes2} }} 
}

print(censo_2017)

"""
B) Crear una nueva clave en cada sub-diccionario llamada “Densidad”. La densidad
poblacional se calcula de la siguiente forma: habitantes / superficie.

"""

# calculo de densidad
densidad1 = habitantes1 / superficie1
densidad2 = habitantes2 / superficie2

print("\n actualizacion de diccionario. \n")

censo_2017["id region1"].update({
    "densidad" : round(densidad1,1)
})

censo_2017["id region2"].update({
    "densidad" : round(densidad2,1)

})

print(censo_2017)

""" C) Agregar otra clave llamada “Capital” en cada sub-diccionario, correspondiente a la
capital de cada región (ver Tabla N°2)"""

capital1 = "valdivia"
capital2 = "punta arenas"

print("\n actualizacion de diccionario. \n")

censo_2017["id region1"].update({
    "capital" : capital1
})

censo_2017["id region2"].update({
    "capital" : capital2

})

print(censo_2017)

"""
D)  Agregar otra clave con el nombre “Comunas” en cada sub-diccionario, la cual será
una lista de 3 comunas de cada región 

"""
comunas1 = ["rio bueno", "la union", "paillaco"]
comunas2 = ["cabo de hornos", "puerto williams", "porvenir"]

print("\n actualizacion de diccionario. \n")

censo_2017["id region1"].update({
    "comunas" : comunas1
})

censo_2017["id region2"].update({
    "comunas" : comunas2

})

print(censo_2017)

"""
E)  Crear una clave llamada “Provincia” en cada sub-diccionario, la cual almacenará los
nombres de las provincias correspondiente a cada región. Las provincias se
guardarán en tuplas

"""
provincias1 = ("ranco", "valdivia")
provincias2 = ("antartica chilena","magallanes", "tierra del fuego", "ultima esperanza")


print("\n actualizacion de diccionario. \n")

censo_2017["id region1"].update({
    "provincias" : provincias1
})

censo_2017["id region2"].update({
    "provincias" : provincias2

})

print(censo_2017)


"""
F)  Actualizar la clave “Nombre Región” en el sub-diccionario correspondiente a
Magallanes, cambiando el valor de “Magallanes” por “Magallanes y Antártica
Chilena”. Utilizar la función correspondiente en Python


"""

act = "magallanes y antartica chilena"

print("\n actualizacion de diccionario con el remplazo \n")

censo_2017["id region2"].update({"nombre region" : "magallanes y antartica chilena"})


# G) imprimir diccionario con el cambio

print(censo_2017)

"""
H) Obtener una lista de tuplas que contengan la clave y el valor de cada elemento del
diccionario con la función correspondiente en Python.

"""
print(list(tuple(censo_2017["id region1"])))
print(list(tuple(censo_2017["id region2"])))

lista_items = list(censo_2017.items())

print(lista_items) 