""" Ingresa 150 carácteres e indicar cuantas veces se repite "a"  """

# solicitantdo datos

#  TEXTO DE 150: "El sol se oculta tras las montañas, pintando el cielo de tonos naranjas y rosas. La brisa suave acaricia los árboles, creando un ambiente de paz y serenidad."
caracteres = str(input("ingrese 150 caracteres: "))
letra_a = []

# si no se cumple la condicion no avanza el código
while len(caracteres) != 150:
    caracteres = str(input("No se han ingresado 150 caracteres, intentelo denuevo. \n"))

for i in caracteres:
    
    if i == 'a':
        letra_a.append(i)

conteo = letra_a.count('a')
if 'a' in letra_a:

    print(f"Según la busqueda el caracter 'a' se encuentra: {conteo} veces")
else:
    print("No se encuentra el carcter 'a' ")