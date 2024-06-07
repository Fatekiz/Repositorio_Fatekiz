#          ---- Ejercicio n2 ----

p1 = int(input("ingrese el año de vencimiento del producto 1: ")), int(input("Ingrese el mes de vencimiento del producto 1: ")), int(input("Ingrese el dia de vencimiento del producto 1: "))
p2 = int(input("ingrese el año de vencimiento del producto 2: ")), int(input("Ingrese el mes de vencimiento del producto 2: ")), int(input("Ingrese el dia de vencimiento del producto 2: "))
p3 = int(input("ingrese el año de vencimiento del producto 3: ")), int(input("Ingrese el mes de vencimiento del producto 3: ")), int(input("Ingrese el dia de vencimiento del producto 3: "))

fecha_ordenada = sorted([p1,p2,p3])
print(fecha_ordenada)