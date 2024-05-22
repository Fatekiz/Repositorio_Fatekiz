# Algoritmo

print("A continuación ingrese las 3 notas de Joel \n") # 1. Joel

notaj1 = float(input("Ingrese la nota numero 1 de Joel: "))
notaj2 = float(input("Ingrese la nota numero 2 de Joel: "))
notaj3 = float(input("Ingrese la nota numero 3 de Joel: "))
print("\n")

print("Ahora ingrese las 3 notas de Alondra \n") # 2. Alondra

notaa1 = float(input("Ingrese la nota numero 1 de Alondra: "))
notaa2 = float(input("Ingrese la nota numero 2 de Alondra: "))
notaa3 = float(input("Ingrese la nota numero 3 de Alondra: "))
print("\n")

print(" Y ahora  ingrese las 3 notas de Paz \n") # 3. Paz

notap1 = float(input("Ingrese la nota numero 1 de Paz: "))
notap2 = float(input("Ingrese la nota numero 2 de Paz: "))
notap3 = float(input("Ingrese la nota numero 3 de Paz: "))
print("\n")

#PROMEDIOS

pj = (notaj1 + notaj2 + notaj3) / 3
pa = (notaa1 + notaa2 + notaa3) / 3
pp = (notap1 + notap2 + notap3) / 3

#imprimiendo promedios
print("Los promedios de cada estudiantes son: \n")

print(f"El promedio de Joel es: {round(pj,3)} \n")
print(f"El promedio de Alondra es: {round(pa,3)} \n")
print(f"El promedio de paz es: {round(pp,3)} \n")

#imprimir nota mínima de cada estudiante
print("A continuación las notas mínimas de cada estudiante: \n")

print (f"La nota mínima de Joel es: {min(notaj1,notaj2,notaj3)}")
print (f"La nota mínima de Alondra es: {min(notaa1,notaa2,notaa3)}")
print (f"La nota mínima de Paz es: {min(notap1,notap2,notap3)}")

#promedio de todos

pf = (pj + pa + pp) / 3
print(f"El promedio de los 3 promedios anteriores es: \n")

print(pf)

""" FINALIZADO """