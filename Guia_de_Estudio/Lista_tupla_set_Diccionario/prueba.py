#creando el diccionario

n1 = str(input("Ingrese el nombre de la persona 1: "))
edad = int(input("Ingrese la edad de la persona 1: "))

n2 = str(input("Ingrese el nombre de la persona 2: "))
edad2 = int(input("Ingrese la edad de la persona 2: "))

n3 = str(input("Ingrese el nombre de la persona 3: "))
edad3 = int(input("Ingrese la edad de la persona 3: "))




nombres = {

    n1:edad,
    n2:edad2,
    n3:edad3

}

print(nombres)


nombres.update({

    "Ignacio" : 19 ,
    

})
nombres.pop(n3)
nombres.pop(edad3)

print(nombres)