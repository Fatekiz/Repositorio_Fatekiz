"""  Crear programa que de el promedio ponderado de 5 pruebas donde: 
la primera vale 20% | la segunda vale 60% | la tercera y cuarta un 10% 
luego el programa imprime si el estudiante aprobo o no tomando un 4.0 como nota de corte
"""

print("Ingrese las 4 notas obtenidas para generar un promedio ponderado: \n")

nota1 = input("Nota N°1: ")
nota2 = input("Nota N°2: ")
nota3 = input("Nota N°3: ")
nota4 = input("Nota N°4: ")
# calculo

nota_final= (nota1 * 0.2) + (nota2 * 0.6) + (nota3 * 0.1) + (nota3 * 0.1)

if nota_final >4.0:
    
    print(f"Usted ha aprobado con un: {nota_final}")

else:
    print(f"Usted ha reprobado con un: {nota_final}")