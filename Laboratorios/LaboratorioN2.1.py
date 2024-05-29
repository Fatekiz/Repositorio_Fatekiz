"""         

Una frutería necesita desarrollar un programa que permita calcular algunas operaciones básicas por la compra de cuatro frutas diferentes.
El local requiere saber el total a pagar porla cantidad de cada fruta comprada

"""
# --- DATOS --- (1)

preciom = int(100)
preciop = int(250)
preciod = int(300)

cantidadm = int(150)
cantidadp = int(80)
cantidadd= int(120)

# --- OPERACIONES Y PRINTS --- (2)
totalm = preciom * cantidadm 
print(f"El precio a pagar por las manzanas es de: ${totalm} " )

totalp = preciop * cantidadp
print(f"El precio a pagar por las Peras es de: ${totalp} " )

totald = preciod * cantidadd 
print(f"El precio a pagar por las Duraznos es de: ${totald} \n" )

# -- Suma entre manzana y pera -- (3a)
sumamp = totalm + totalp
print(f"Si solo compra las manzanas y las peras, el total a pagar sería de: ${sumamp} \n")

# --- valor maximo --- (3b) 
valor_max = max(totalm, totalp, totald)
print(f"El valor máximo de los 3 totales es: ${valor_max}")

# --- Valor minimo --- (3c)
valor_min = min(totalm,totalp,totald)
print(f"El valor mínimo de los 3 totales es: ${valor_min} \n")

# --- promedio de los precios unitarios --- (3d)
promedio_unitario = (preciom + preciop + preciod) /3
promedio_unitario = round(promedio_unitario,2)
print(f"El promedio de los precios unitarios de las 3 frutas es: ${promedio_unitario}")