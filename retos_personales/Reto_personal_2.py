# Reto donde el usuario va indicando su nombre y se le entrega una impresion con los datos actualizandose a medida que el entrega info.

print("Bienvenido usuario, para crear su ficha medica, debe indicarnos sus datos a continuacion \n")

#Solicitando datos 

nombre = input("Ingrese su primer nombre: ")

if nombre != str:

    while nombre != str:
        nombre = input("Debe ingresar  su numbre sin numeros. Vuelva a ingresar su primer nombre: ")
    
        break

    print(nombre)