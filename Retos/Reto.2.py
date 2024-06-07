#                                                           RETO NUMERO 2


# asignaturas (para ir en tupla)
asignatura1 = "ingles"
asignatura2 = "matematicas"
asignatura3 = "programacion"

# notas 1 para ir en sets
nota1_1 = 5.5
nota1_2 = 4 
nota1_3 = 5.7

# calculo 1 para la ponderacion de cada nota
notap11 = nota1_1 *0.3
notap12 = nota1_2 *0.5
notap13 = nota1_3 *0.2

# agrupando para mostrar notas
notas1 = {nota1_1,nota1_2,nota1_3}

#promedio ponderado 1
pp1 = {notap11,notap12,notap13}

# notas 2 para ir en sets
nota2_1 = 5.1 
nota2_2 = 7
nota2_3 = 3.4

# ponderacion nota 2
notap21 = nota2_1 *0.3
notap22 = nota2_2 *0.5
notap23 = nota2_3 *0.2

# mostrar notas 2 
notas2 = {nota2_1, nota2_2, nota2_3}

# promedio ponderado 2
pp2 = {notap21,notap22,notap23}

# Notas 3
nota3_1 = 2.1
nota3_2 = 6.8
nota3_3 = 7

# ponderaciones 3
notap31 = nota3_1 *0.3
notap32 = nota3_2 *0.5
notap33 = nota3_3 *0.2

# mostrar notas 3
notas3 = {nota3_1, nota3_2, nota3_3}

# promedio ponderado notas 3
pp3 = {notap31,notap32,notap33}

#Calculo para promedio
pnotas1 = sum(pp1)
ppnotas1 = round(pnotas1,1)

pnotas2 = sum(pp2)
ppnotas2 = round(pnotas2,1)

pnotas3 = sum(pp3)
ppnotas3 = round(pnotas3,1)


#tuplas finales
tupla1 = (asignatura1,notas1,ppnotas1)
tupla2 = (asignatura2,notas2,ppnotas2)
tupla3 = (asignatura3,notas3,ppnotas3)


info = {
    "Benjamin" :  [ tupla1 , tupla2, tupla3

     ]

}

print(info)
nombre = str(info)


print(f"Detalles de el alumno {nombre} \n en su asignatura: {asignatura1} obtuvo las notas:{notas1} y de promedio: {ppnotas1} \n en su asignatura: {asignatura2} obtuvo las notas:{notas2} y de promedio: {ppnotas2} \n en su asignatura: {asignatura3} obtuvo las notas:{notas3} y de promedio: {ppnotas3}")