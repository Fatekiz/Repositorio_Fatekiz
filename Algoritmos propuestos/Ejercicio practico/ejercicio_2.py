# hacer piramide de numeros 

print(f"         1         ")
print(f"        232        ")
print(f"       34543       ")
print(f"      4567654      ")
print(f"     567898765     ")
print(f"    67890109876    ")
print(f"   7890123210987   ")
print(f"  890123454321098 ")
print(f" 90123456765432109 ")
print(f"0123456789876543210")


# forma 2 "for"

niveles = 10

for i in range(1, niveles +1):
    numeros= []
    for j in range(i):
        numeros.append(str((i + j) % 10))
    for j in range(i -2, -1, -1):
        numeros.append(str((i + j) % 10))
    linea = " ".join(numeros)
    print(linea.center(niveles * 4 - 3))

    # BRIGIDO...