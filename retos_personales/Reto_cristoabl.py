# Crear una tienda con diferentes productos y a cada productos agragar precios, luego hacer un promedio de todo el inventario, y restar el valor mas bajo.
print("\n")

print("---- INGRESE PRODUCTOS PARA QUE SE AGREGEN A LA TIENDA ---- \n ")

producto1 = (input("Ingrese el nombre de un producto "))
preciop1 = float(input("Ingrese el precio del producto: "))

producto2 = (input("Ingrese el nombre de un producto "))
preciop2 = float(input("Ingrese el precio del producto: "))

producto3 = (input("Ingrese el nombre de un producto "))
preciop3 = float(input("Ingrese el precio del producto: "))

producto4 = (input("Ingrese el nombre de un producto "))
preciop4 = float(input("Ingrese el precio del producto: "))

producto5 = (input("Ingrese el nombre de un producto "))
preciop5 = float(input("Ingrese el precio del producto: "))

#promedio

promedio = (preciop1 + preciop2 + preciop3 + preciop4 + preciop5) / 5 

print(f"El promedio del inventario es: {promedio}")

#promedio final
promediof = promedio - min(precios)

#impr el resultado final

print(f" La resta da:$ {promediof}")