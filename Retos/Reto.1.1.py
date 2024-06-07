# Correción del algoritmo

#preguntando por consola y asignar a las variables
nombre = input("¿Cual es su nombre? ")
edad = int(input("¿Cual es su edad? "))

# operacion entre edad + 20 años
suma = edad + 20

#imprimir resultado de todo
print(f" Hola mi nombre es {nombre} es tengo {edad} y en 20 años más tendré {suma} años ")

# OBSERVACION:  1.- (LINEA 11) Ocupé el print(f" x {} ") y me di cuenta que es más eficiente
#               2.- (LINEA 5) Hice mas eficiente el codigo ocupando un int(input("x"))  para asignar el valor de un ENTERO al número que se asigne