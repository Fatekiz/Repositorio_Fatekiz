#                                       Ejercicio Num4


#Solicitando los valores por consola

name1 = input("Ingrese el nombre de la persona n1 ")
edad1 = int(input("Ingrese la edad de la persona n1 "))

name2 = input("Ingrese el nombre de la persona n2 ")
edad2 = int(input("Ingrese la edad de la persona n2 "))

name3 = input("Ingrese el nombre de la persona n3 ")
edad3 = int(input("Ingrese la edad de la persona n3 "))

infos = {

    name1: edad1,
    name2: edad2,
   name3: edad3
}
print(f"Diccionario de personas \n")
print(f"{name1}: {infos[name1]} años")
print(f"{name2}: {infos[name2]} años")
print(f"{name3}: {infos[name3]} años")

# Agregando persona al diccionario
new_name = input("Ingrese el nombre de una nueva persona: ")
new_edad = int(input(f"Ingrese la edad de {new_name}"))
infos[new_name] = new_edad

# Eliminar una persona del diccionario

persona_a_eliminar = input("ingrese el nombre de la persona a eliminar: ")
del infos[persona_a_eliminar]

# Mostrando diccionario actualizado

print("Diccionario actualizado")

nombres = list(infos.keys())
edades = list(infos.values())

print(f"{nombres[0]}: {edades[0]} años.")
print(f"{nombres[1]}: {edades[1]} años.")
print(f"{nombres[2]}: {edades[2]} años.")