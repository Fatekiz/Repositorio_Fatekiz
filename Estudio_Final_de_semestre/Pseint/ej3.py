# crear un programa que al ingresar 2 numeros haga una operacion matematica segun los numeros
# si los números son iguales: se multiplican
# si el  primer numero es mayor al segundo: se suman
# si el primero es menor que el segundo se restan

p_num = int(input("Ingrese el primer numero: "))
s_num = int(input("Ingrese el seundo numero: "))

if p_num == s_num:
    print(f"los numeros son iguales, se multiplicaron y el resultado es: {p_num*s_num}")
elif p_num > s_num:
    print(f"El primer numero es mayor, se sumaron y el resultado es: {p_num+s_num}")
else:
    print(f"El primer numero es menor, se restaron y el resultado es: {p_num - s_num}")

 # Terminado