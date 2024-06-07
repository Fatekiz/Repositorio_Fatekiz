# inicializando las categorias de los animales en sets

aves = {"Aguila", "Pato", "Canario"}
Animales_Terrestres = {"Leon", "Elefante", "Nutria"}
Animales_Acuaticos = {"Pato", "Delfin", "Nutria"}

aves.add("Pajaro")
Animales_Terrestres.add("Perro")
Animales_Acuaticos.add("Pescado")

print(aves)
print(Animales_Acuaticos)
print(Animales_Terrestres)

print(f"{aves.intersection(Animales_Terrestres)}<-- No hay animales repetidos entre Aves y animales Terrestres")
print(f"{aves.intersection(Animales_Acuaticos)}<--  animal repetido entre Aves y animales Acuaticos")
print(f"{Animales_Acuaticos.intersection(Animales_Terrestres)}<--  animal repetido entre Animales acuaticos y animales Terrestres")