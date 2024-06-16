# GUIA DE BUCLES

#llamando bibloteca
from colorama import init, Fore


num = 0 

print(Fore.BLUE + "Inicio de Ciclo N°1")
while num <= 100:
    print(num)
    # num = num +2
    num +=  2 # <--- el "+=" es una abreviación de
print(Fore.BLUE + "Termino Ciclo N°1")


print(Fore.CYAN + "Inicio de Ciclo N°2")
while num <= 200:
    print(num)
    
    num +=  2 
else:
    print(Fore.RED + "El numero sobre paso el num 200")
print(Fore.CYAN + "Termino Ciclo N°2")

print(Fore.MAGENTA + "Inicio de Ciclo N°3")
while num <= 300:
    print(num)
    num +=  2 
    if num == 250:
        print(Fore.YELLOW + "se detiene la ejecución")
        break
print(Fore.CYAN + "Termino Ciclo N°3")

# ciclo for 
new_lista = [1,2,3,4,5,6,7,8,9,10]

print(Fore.GREEN + "Inicio de chilo N4 (FOR)")

for i in new_lista:
    print(i)

print(Fore.LIGHTBLUE_EX + "Inicio de chilo N5 (FOR)")
for i in range(1,11):
    print(i)

