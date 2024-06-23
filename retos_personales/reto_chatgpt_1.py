numero = int(input("ingrese un numero entero positivo y se hará la multiplicacion de este."))

for i in range(1,numero + 1):
    resultado = numero * i
    print(f"resultado de {i} x {numero} = {resultado}")