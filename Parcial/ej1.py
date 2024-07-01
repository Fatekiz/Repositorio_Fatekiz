"""
Se cuenta con dos sets: el primero contiene las temperaturas mínimas tomadas el mes de
Mayo en Castro. El segundo set contiene las temperaturas máximas del mes de Mayo en
Castro. (60 Puntos)

● Temperaturas Mínimas = {9, 5, 2, 7, 6, 1}
● Temperaturas Máximas = {12, 14, 11, 10, 15, 9}

A) Verificar si la temperatura 9°C se encuentra en ambos sets utilizando condicionales.

B) Unir ambos sets en un solo y eliminar duplicados. Imprimir el set generado.

C) Transformar el set en una lista, y encontrar las temperatura mínima y máxima
utilizando bucles. Imprimir los resultados.

D) Crear una tupla con los valores de temperaturas mínima y máxima, más un string
con las etiquetas de texto: “Mínima” y “Máxima”. Imprimir la tupla generada.

E) Generar e imprimir un diccionario donde las claves sean las temperaturas y los valores sean la frecuencia de aparición.

"""

# VARIABLES

temp_min = {9, 5, 2, 7, 6, 1}
temp_max = {12, 14, 11, 10, 15, 9}

# A) Verificar si la temperatura 9°C se encuentra en ambos sets utilizando condicionales. (listo)

if 9 in temp_min and 9 in temp_max:
    print("\n La temperatura: '9' se encuentra en ambos sets.")
else:
    print("\n la temperatura: '9' no se encuentra en ambos sets")


# B) Unir ambos sets en un solo y eliminar duplicados. Imprimir el set generado. (listo)

temps_unidas = temp_min.union(temp_max)
print(f"\n Todas las temperaturas unidas en un Set: {temps_unidas}")


# C) Transformar el set en una lista, y encontrar las temperatura mínima y máxima utilizando bucles. Imprimir los resultados. # tupla con minima y maxima (lista)
temp_unidas = list(temps_unidas)

minima = 100
for i in temp_unidas:
    
    if i < minima:
        minima = i


maxima = 0
for i in temp_unidas:
    
    if i > maxima:
        maxima = i

print(f"\n La temperatura 'minima' de todas las registradas es de: {minima} grados. y la tempera 'máxima' es de: {maxima} grados.")

# D) Crear una tupla con los valores de temperaturas mínima y máxima, más un string con las etiquetas de texto: “Mínima” y “Máxima”. Imprimir la tupla generada. (lista)

tupla = (str("Mínima"), int(minima), str("Máxima"), int(maxima))
print(f" {tupla} \n")

# E) Generar e imprimir un diccionario donde las claves sean las temperaturas y los valores sean la frecuencia de aparición.

# keys: temps
# values: frec
# temp_unidas


diccionario1 = {0 : 100,1 : 101,2 : 102,3 : 103,4 : 104,5 : 105,6 : 106,7 : 107,8 : 108,9 : 109,10 : 110,}

for i in temp_unidas:
    contador = 0
    contador2 = 100
    contador = i
    contador2 = temp_unidas.count(i)
    diccionario1.update(contador = contador2)
    contador+=1
    contador2+=1

print(diccionario1)