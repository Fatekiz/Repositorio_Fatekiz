"""pedir una serie de numero y sumarlo en la salida"""

#pidiendo dato
num = int(input("Ingrese una serie de numero para poder sumar sus digitos "))

# inicio de bucle
suma = 0
for i in str(num): # convierto a str los numeros para usarlos
    suma += int(i) # vuelvo a convertir a int pero el "i" ya que el recorrerá cada digito
print(suma)

#terminado