# hacer un diccionario para un sistema de registro social


#hacemos la funcion para el menu principal
def menu():
    print("\n bienvenido a sistema de registro social\n ")
    print("escoja la opcion que usted desee para ejecutar el programa")
    print("opciones: ")
    print("1.- agregar personas y sus datos")
    print("2.- mostrar toda la gente y sus datos")
    print("3.- Salir del programa.")
    x = input("Ingrese la opcion: ")
    return x


# def para agregar persona
def agregar_persona(registro_social):

    print("ingrese el nombre de la persona")
    nombre = input("Nombre: ")
    print("Ciudad de nacimiento")
    ciudad = input("nombre de la ciudad: ")
    print("su edad")
    edad = input("edad: ")
    registro_social["nombre"] = nombre
    registro_social["ciudad"] = ciudad
    registro_social["edad"] = edad
    print("--- Datos  agregados. --- ")

# funcion para mostrar registro social
def mostrar_registro(registro_social):
    if not registro_social:
        print("\n  --- ERROR: No hay personas agregadas. --- ")
    else:
        for dato,dato2,dato3  in registro_social.keys():
            print(f"nombre:{dato}")
            print(f"ciudad:{dato}")
            print(f"edad:{dato}")

# programa prinicpal

def main():
    registro_social = {}
    while True:
        opcion = menu()
        if opcion == "1":
            agregar_persona(registro_social)
        elif opcion == "2":
            mostrar_registro(registro_social)
        elif opcion == "3":
            print("\n saliendo del programa... \n")
            break
        else:
            print("\n --- opcion no valida. Porfavor intente denuevo. --- \n")

if __name__ == "__main__":
    main()