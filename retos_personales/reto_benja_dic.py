# hacer un diccionario para un sistema de registro social


#hacemos la funcion para el menu principal
def menu():
    print("bienvenido a sistema de registro social")
    print("escoja la opcion que usted desee para ejecutar el programa")
    print("opciones: \n")
    print("1.- agregar personas y sus datos")
    print("2.- mostrar toda la gente y sus datos")
    print("3.- Salir del programa.")
    opcion = input("Ingrese la opcion: ")
    return opcion


# def para agregar persona
def agregar_persona(registro_social):
    registro_social = {"nombre":nombre,"ciudad":ciudad, "edad":edad}
    print("ingrese el nombre de la persona")
    nombre = input("Nombre: ")
    print("Ciudad de nacimiento")
    ciudad = input("nombre de la ciudad: ")
    print("su edad")
    edad = input("edad: ")
    print("calificaciones agregadas.")

# funcion para mostrar registro social
def mostrar_registro(registro_social):