"""Objetivo:
Escribir un programa en Python que almacene las calificaciones de varios estudiantes en un diccionario. 
El programa debe permitir agregar calificaciones y mostrar todas las calificaciones almacenadas."""

# funcion para mostrar el menu al usuario
def mostrar_menu():
    print("1.- agregar calificacion al estudiante")
    print("2.- Mostrar todas las calificaciones")
    print("3.- Salir")
    x = input("ingrese una opción ")
    return x

# funcion para agregar la calificacion a un estudiante
def agregar_calificacion(calificaciones):
    nombre = input("ingrese el nombre del estudiante ")
    calificacion = int(input(f"Ingrese la calificacion de {nombre} "))
    calificaciones[nombre] = calificacion
    print("calificacion agregada. \n")

# funcion para mostrar todas las calificaciones
def mostrar_calificaciones(calificaciones):
    if not calificaciones:
        print("No hay calificaciones agregadas")
    else:
        print("calificaciones:")
        for nombre,calificacion in calificaciones.items():
            print(f"{nombre}: {calificacion}")
        print("")

# El programa principal

def main(): 
    calificaciones = {}
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            agregar_calificacion(calificaciones)
        elif opcion == "2":
            mostrar_calificaciones(calificaciones)
        elif opcion == "3":
            print("saliendo del programa...")
            break
        else:
            print("Opcion no válida. Porfavor intente denuevo. \n ")

if __name__ == "__main__":
    main()

# Brigido... apenas lo entiendo