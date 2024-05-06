
#1. Declarando Variable con el x = "y"
name = "Benjamin"
apellido = "Concha"
edad = 18

#2. impresion de la variable (print clasimo)
print("1. Hola soy", name)

#3. Impresión de variable (print f-string)
print(f"2. Hola mi nombre es {name}") 

# 4. Impresión de variable (concatenación)
print("3. ¡Hola buenas! yo soy " + name + " " + apellido  + " y tengo" + " " + str(edad) +" " + "años" )

#5. Declarando variable numérica
edad = 18
cumpleaños = 2005
estatura = 1,71
peso = 58.4
n_comp = 5 + 4j
n_comp2 = complex(5,4)

#6. imprimiendo numeros
print("4. mi edad es de: " + str(edad) + " años Y mi estatura es de: " + str(estatura) + " M")
#Formateando la salida de números
pi = 3,14159

# 7. Variables en una sola linea (No es tan recomendado para depurar)
pais, region, ciudad, codigo_postal = "Chile", "Los Lagos", "Castro", 5780000
print(pais, region, ciudad, codigo_postal )

# 8. imput

year = input("en que año naciste?")
print("el año de nacimiento es: " + year)