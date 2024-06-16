
#                                     SENTENCIAS CONDICIONALES

# Caracteristicas: Las condicionales permiten  comprobar condiciones y hacer que nuestro programa se comporte de una
# manera u otra, que se ejecute un fragmento de código  en específico, dependiendo de esta condición
# Las estructuras de control nos ofrecen la posibilidad de modificar el curso de ejecución de un algoritmo



""" 
Para declarar condiciones o bifurcaciones, se utiliza la funcion if:

y cuando queremos preguntar cúando "NO SE CUMPLE" la condicion anterior, como (de lo contrario)  

"""

# IF
#


#Ejemplo:
edad1 = 19

if edad1 >= 18:
    print("eres mayor de edad.")
else:
    print("eres menor de edad.")
print("Este print esta fuera del if") # <--- no se indentó (indentar), por ende no funcionara dentro del if

# Ejemplo 2:
edad_benja = 18

if edad_benja >= 18 and edad_benja < 65:
    print("Eres mayor de edad")
elif edad_benja > 65:
    print("eres un adulto mayor.")
else:
    print("Eres menor de edad")



#              OPERADORES TERNARIOS
"""
El operador ternario permite hacer una condicion con una sola linea.


"""
edad3 = 20

print("Usted puede votar" if edad1 >= 18 else "Usted no puede votar."        ) # <-- los programadores senior ocupan esto.


#         BUCLES/CICLOS/LOOPS








#         while (mientras)
"""
Este tipo de ciclo permite ejecutar


"""


#WHILE INFINITO (NO HACER):

# while True
#   print(num)                  <--- NO HACER ESTO ya que es un bucle infinito, en resumenno tiene un termino.
#   num +=2

#                        ctrl + c | para salir de un bucle infinito.


#                    WHILE (ELSE/IF)
num = 20
while num <= 100:
    print(num)
    num += 2
else:
    print("mi variable es igual o mayor a 100")


while True:
    parametro = input(">")
    if parametro == "exit": # <-- hasta que yo escriba "exit" en terminal
        break
    else:
        print(parametro)



"""
    edad no valida < 0
    niño/a <= 12
    adolecente <= 17
    adulto <=64
    adulto mayor <= 120
    Edad no válida >= 120
"""

edad = int(input("ingrese la edad de la persona: "))

if edad <= 0 or edad >= 120:
    categoria = "Edad no válida"
elif edad <= 12:
    categoria = "Niño/a"
elif edad <= 17:
    categoria = "adolecente"
elif edad <= 65:
    categoria = "adulto"
else:
    categoria = "adulto mayor"

print(f"La persona es: {categoria}")