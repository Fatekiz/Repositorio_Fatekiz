# Crear programa que cree un contador de vocales
contador = 0
vocales = "aeiouAEIOU"
frase = str(input("Ingrese una frase y le diremos cuantas vocales tiene: "))

for i in frase:
    if i in vocales:
        contador+=1
        
print(f"su frase cuenta con: {contador} vocales.")