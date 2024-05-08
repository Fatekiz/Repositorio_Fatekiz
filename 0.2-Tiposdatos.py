#Tipos de datos


# 1. STRINGS
institucion = "Universidad de Los Lagos"
asignatura = "Programación"
descripcion = """Asignatura del primer semestre de la ingieneria 
civil en informatica"""

#imprimir la posición de un carácter
print("1.-", institucion[1])

#concatenacion
resultado = print("2.-", institucion + " " +  asignatura)

# Multiplicando el texto por un número
print("3.-",asignatura *4)

#División de cadena (split)

print("4.-",institucion.split())

#aplicando len()

print("5.-", len(asignatura))