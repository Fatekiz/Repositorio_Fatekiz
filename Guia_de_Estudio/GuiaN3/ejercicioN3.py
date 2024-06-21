""" 
3. Tres empleados de una fabrica trabajan en dos turnos: diurno y nocturno (10 hrs cada uno). 
Se busca calcular el pago diario y el total semanal de cada empleado de acuerdo con los siguientes puntos:
a) La tarifa del turno diurno por hora es de 12000 CLP.
b) La tarifa del turno nocturno por hora es de 16000 CLP.
c) Los domingos la tarifa se incrementa en 2000 CLP el turno diurno y 3000 CLP el
turno nocturno.


Ademas considerar: 

a) El primer empleado trabaja Lunes, Martes y Miercoles en turnos nocturnos, Jueves
y Viernes en turnos diurnos.

b) El segundo empleado trabaja Martes, Miercoles y Jueves turnos nocturnos, y tambien el dia domingo en turno diurno.

c) El tercer empleado trabaja Miercoles, Jueves y Viernes diurno, Sabado y Domingo 
en turnos nocturnos.

Guardar la informacion de cada empleado en un diccionario, con el pago diario que debe 
recibir cada empleado y el total de la semana.

"""
#Tarifas por hora según turnos
tarifa_h_d = 12000 # por hora
tarifa_h_n = 16000
aumento_d_d = (tarifa_h_d + 2000) # por hora
aumento_d_n = (tarifa_h_n + 3000)

# Pago semanal de Juan
pago_s_juan = ((tarifa_h_n * 3) + (tarifa_h_d * 2))

# pago semanal de diego:
pago_s_diego = ((tarifa_h_n*3) + aumento_d_d)

# pago semanal de benja
pago_s_benja = ((tarifa_h_d*3) + tarifa_h_n + aumento_d_n)


# Diccionario

sueldos_de_empleados = {

    "empleado_1" : "juan",
    "pago_ds_1" :  
        {
           "pagos_diarios" :
           {
           "lunes" : tarifa_h_n,
            "martes" : tarifa_h_n,
            "miercoles" : tarifa_h_n,
            "jueves" : tarifa_h_d,
            "viernes" : tarifa_h_d,
           },
           "pago_semanal" : {"pago_semanal" : pago_s_juan}
        },

    "empleado2" : "diego",
    "pago_ds_2" :  
        {
           "pagos_diarios" :
           {
           "martes" : tarifa_h_n,
            "miercoles" : tarifa_h_n,
            "jueves" : tarifa_h_n,
            "domingo" : aumento_d_d
           },
           "pago_semanal" : {"pago_semanal" : pago_s_diego}
        },

    "empleado3" : "benjamin",
        "pago_ds_3" :  
        {
           "pagos_diarios" :
           {
           "miercoles" : tarifa_h_d,
            "jueves" : tarifa_h_d,
            "viernes" : tarifa_h_d,
            "sabado" : tarifa_h_n,
            "domingo" : aumento_d_n
           },
           "pago_semanal" : {"pago_semanal" : pago_s_benja}
        },


}
print(sueldos_de_empleados["pago_ds_1"]) # info de sueldo de juan
print(sueldos_de_empleados["pago_ds_2"]) # info de sueldo de diego
print(sueldos_de_empleados["pago_ds_3"]) # info de sueldo de benjamin

# Terminado