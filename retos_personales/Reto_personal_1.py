# esto es solo algo provicional para practicar.
# RETO_PERSONAL_1
# haga un sistema de promedios donde se ingrese las notas y se promedien para un promedio final
#promedio: nota 1 (30%) nota 2 (30%) ppt (20%) proyecto (20%)

print("-------------------------------------------------------")
#bienvenida e indicaciones
print("Hola Usuario, indique sus notas para realizar su promedio")

print("") #espacio

#solicitud de notas
nota1 = float(input(f"indique su nota numero 1 | "))
print(f"Nota ingresada: {nota1}")

print("")

nota2 = float(input(f"indique su nota número 2 | "))
print(f"Nota ingresada: {nota2}")
print("")

ppt = float(input(f"indique la nota del ppt | "))
print(f"Nota ingresada: {ppt}")

print("")

proyecto = float(input(f"indique la nota de su proyecto |"))
print(f"nota ingresada: {proyecto}")
print("")

# Calculo matemático
notaf = (nota1 * 0.3) + (nota2 *0.3 ) + (ppt * 0.2) + (proyecto * 0.2) 

#impresion de promedio
print(f"Usuario, su promedio es de {notaf}")

# RETO PERSONAL TERMINADO!!