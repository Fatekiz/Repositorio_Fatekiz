# Reto donde el usuario va indicando su nombre y se le entrega una impresion con los datos actualizandose a medida que el entrega info.

print("Bienvenido usuario, para crear su ficha medica, debe indicarnos sus datos a continuacion \n")

ficha_medica = []
#Solicitando datos 

nombre = input("Ingrese su primer nombre: ")
print(f"nombre entregado {nombre}")
ficha_medica.append(nombre)

apellido = input("Ahora indicanos tu apellido: ")
print(f"Apellido entregado: {apellido}")
ficha_medica.append(apellido)


edad = input("Ingresa tu edad: ")
print(f"La edad proporcionada es: {edad}")

ficha_medica.append(edad)

fechanacimiento = input("Ingresa la fecha de tu nacimiento: (dd/mm/aaaa) ")
print(f"Tu fecha de nacimiento es: {fechanacimiento}")

ficha_medica.append(fechanacimiento)

ficha_medica = " " .join(ficha_medica)

print(f"Datos: {ficha_medica}")