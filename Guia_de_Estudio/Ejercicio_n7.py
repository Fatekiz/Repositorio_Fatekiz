"""
Se necesita planificar el esquema de notas de la asignatura de Programación. Desarrollar un
algoritmo que permita ingresar el nombre de un estudiante, su carrera y las notas de dos
laboratorios de tres estudiantes.

 Almacenar las notas en tuplas y los estudiantes en un diccionario. Mostrar las notas de cada estudiante.

a. Ingresar los nombres, carrera de los estudiantes y las notas de los dos exámenes por
consola.

b. Almacenar las calificaciones en tuplas y los datos de los estudiantes en un
diccionario.

c. Imprimir el nombre, carrera y las notas de cada estudiante.


"""

carrera = input("Ingrese el nombre de la carrera: ")
n1 = input("Ingrese el nombre del primer estudiante: ")
nota1_1 = input("ingrese la primera nota del estudiante en lab: ")
nota1_2 = input("ingrese la segunda nota del estudiante en lab: ")
n2 = input("Ingrese el nombre del segundo estudiante: ")
nota2_1 = input("ingrese la primera nota del estudiante en lab: ")
nota2_2 = input("ingrese la segunda nota del estudiante en lab: ")
n3 = input("Ingrese el nombre del tercer estudiante: ")
nota3_1 = input("ingrese la primera nota del estudiante en lab: ")
nota3_2 = input("ingrese la segunda nota del estudiante en lab: ")



programacion = {
    
    "carrera" : carrera,
    
    "estudiante1" : n1,
    "estudiante2" : n2,
    "estudiante3" : n3
}

notas_estudiante_1 = (nota1_1,nota1_2)
notas_estudiante_2 = (nota2_1,nota2_2)
notas_estudiante_3 = (nota3_1,nota3_2)

print(f"Datos de estudiante 1: \n")
print(f"{programacion['estudiante1']} | carrera: {programacion['carrera']} | notas: {notas_estudiante_1} \n")

print(f"Datos de estudiante 2: \n")
print(f"{programacion['estudiante2']} | carrera: {programacion['carrera']} | notas: {notas_estudiante_2} \n")

print(f"Datos de estudiante 3: \n")
print(f"{programacion['estudiante3']} | {programacion['carrera']} | notas: {notas_estudiante_3} \n ")