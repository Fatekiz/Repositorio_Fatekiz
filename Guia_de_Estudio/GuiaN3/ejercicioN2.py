
secuencia = [500]
inicio_num = 44
op_sum = False ###alterna con el no
#### para cambiar de false y True en funcion de resta y suma
#####el -1 para que comience desde el anterior resultado
while secuencia[-1] < 800:
    if op_sum:
        siguiente_numero = secuencia[-1] + inicio_num
    else:
        siguiente_numero = secuencia[-1] - inicio_num

    secuencia.append(siguiente_numero) ####añade los numeros a la secuencia 
    op_sum = not op_sum
    #como el patron aumenta en 10 al sumar y 2 mas al restar
    if op_sum:
        inicio_num += 10
    else:
        inicio_num += 2
suma= sum(secuencia)
print(secuencia)
print(f"la suma total de la secuencia es de: {suma}")

# terminado