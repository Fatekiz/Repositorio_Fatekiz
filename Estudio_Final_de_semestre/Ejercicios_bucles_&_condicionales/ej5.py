# hacer un programa que encuentre el número máximo de una lista dada usando bucle for

numeros = [2,7,4,3,9,8,6]
num_max = 0

# creando bucle
for i in numeros:
    if i > num_max:
        num_max = i
print(f"El numero mayor de la lista es: {num_max}")