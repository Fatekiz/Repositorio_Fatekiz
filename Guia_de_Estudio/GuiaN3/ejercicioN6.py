"""6. Simular el comportamiento de un reloj digital, imprimiendo la hora, minutos y segundos
de un dia desde las 00:00:00 horas hasta las 23:59:59 horas.
"""

# defino mis variables y que comiencen en 0
hora = 0
minuto = 0
segundo = 0


while hora != 24: #mientras la variable hora sea distinta a 24 entonces...
    print(f"{hora:02}:{minuto:02}:{segundo:02}")    #  printiar la hora desde el comienzo que es 00:00:00 | segun lo que estudié si ocupamos la variable seguida de ":" significa
                                                   # que se formatea, segui del "02" que significa que los numeros tendrán formatos de 2 dígitos, si le falta, el lado izq se
                                                   # llenará con un 0 | aparte ocupo el f-string para así poder separar con ":"                         
    
    segundo += 1 # ir sumando segundos y luego volver arriba, hasta que se cunpla lo de abajo
    if segundo == 60: # si el contador de los segundos llega a 60 se cambia la variable a 0 y se suma un minuto, de esta manera vuelve hacia arriba.
        segundo = 0
        minuto +=1
        if minuto == 60: # lo mismo que el "if" de arriba solo que con las horas.
            minuto = 0
            hora += 1

# Ejercicio terminado.