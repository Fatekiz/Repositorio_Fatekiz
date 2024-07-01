"""
Desarrollar un algoritmo que solicite al usuario una cadena de texto y cuente cuántas veces
aparecen las vocales 'a', 'e', 'i', 'o' y 'u' en la cadena de texto. Utilizar ciclos para resolver el
problema
"""

def encuentraletra(texto, letra): # x será la vocal.
    contador = 0
    for i in range(len(texto)):
        if texto[i] == letra:
            contador+=1
    return contador


print("Bienenido usuario, a continuación ingrese una cadena de texto para que sus vocales sean contadas.")

text = str(input("INGRESE AQUÍ EL TEXTO: "))

print(f"la letra 'a' se encuentra {encuentraletra(text,'a')} veces. la letra 'e' se encuentra {encuentraletra(text,'e')} veces. la letra 'i' se encuentra {encuentraletra(text,'i')} veces. la letra 'o' se encuentra {encuentraletra(text,'o')} veces. la letra 'u' se encuentra {encuentraletra(text,'u')} veces.")
