# Reto actualizado y retroalimentado por José
# diferencia: probaré haciendoló con inputs

print("A continuación ingrese los datos para mostrar la información de un estudiante y sus notas")

nombre = input("Ingrese el nombre del estudiante: ")

info1 = {
"nombre" : nombre, 
"Asignatura" : str(input("Ingrese el nombre de la asignatura ")),
"nota1" : float(input("Ingrese la nota 1: ")),
"nota2" : float(input("Ingrese la nota 2: ")),
"nota3" : float(input("Ingrese la nota 3: "))

}



dict_fin = {

    nombre : [ (info1["Asignatura"]   ,  {info1["nota1"],info1["nota2"],info1["nota3"]} ,   round(info1["nota1"]*0.3 + info1["nota2"]*0.5 + info1["nota3"]*0.2 , 1)      )],
    
    

}

print(dict_fin)

# FALTA TERMINAR