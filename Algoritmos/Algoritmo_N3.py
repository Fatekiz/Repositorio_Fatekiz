# Algoritmo N3

#bienvenida
print("\n") #Enter

print("--¡Bienvenido!-- \n")
print("ingrese las descripciones de los dos productos")
print("Recuerde que la descripción debe tener minimo 40 caracteres \n")

#pidiendo datos por consola
art1 = str(input("Ingrese la descripción del artículo >Silla< (Mínimo 40 carácter) \n"))
 
while len(art1) < 40:
    print("(Recuerde que debe ser mínimo 40 carácteres)")
    art1 = input("Ingrese la descripcion del articulo ""Silla"" \n")

print("\n")

art2 = str(input(" Ahora ingrese la descripción del articulo ""Laptop"" \n"))

while len(art2) < 40:
    print("(Recuerde que debe ser mínimo 40 caráctere \n)")
    art2 = str(input("Ingrese la descripciónp del articulo ""Laptop"" \n"))

print("\n")
print("ahora ingrese el valor y cantidad de cada artículo \n")

valorY = int(input("Ingrese el Valor del producto ""Silla"" "))
cantidadY = int(input("¿Cuanta cantidad hay del articulo ""Silla""? "))

valorM = int(input("Ingrese el valor del producto ""Laptop"" "))
cantidadM = int(input("¿Cuanta cantidad hay del articulo ""Laptop""? "))

print("\n")

# Utilizando el upper
art11 = art1.upper() 
art22 = art2.upper()

print(f"{art1} {art2}")

sumaY = (cantidadY * valorY)
sumaM = (cantidadM * valorM)
suma = sumaY + sumaM
print(f"el valor total de el inventario con los dos productos es de: {suma}")



promedio = (valorM + valorY) / 2

print(f"el precio promedio entre los dos productos es de: {promedio} " )
