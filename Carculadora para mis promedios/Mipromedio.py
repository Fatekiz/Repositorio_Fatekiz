#                                                --------  CARCULADORA PARA MIS PROMEDIOS  --------

#codigo basado para nota1(x%) + nota2(x%) + nota Parcial(x%) / 3 = promedio final

print("Ingresa tus notas para obtener tu promedio \n")

#          ----  Pidiendo notas  ----
nota1 = float(input("Ingresa la nota 1:  "))
print(f"nota ingresada {nota1} \n")

nota2 = float(input("Ingresa la nota 2:  "))
print(f"nota ingresada {nota2} \n")

notap = float(input("Ingresa la nota del parcial:  "))
print(f"nota ingresada {notap} \n")

#          ----  calculo  ----
promedio_final = 0.3 * nota1 + 0.3 * nota2 + 0.4 * notap

print(" \n")

print(f"TU PROMEDIO FINAL ES: {promedio_final}")