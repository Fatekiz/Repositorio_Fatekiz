"""
Determinar si una palabra ingresada por teclado es un palíndromo. Eliminar espacios y
convertir el texto ingresado a minúsculas. Además, imprimir la palabra invertida. (40 Puntos)
Un palíndromo es una palabra o frase que se lee igual de izquierda a derecha que de derecha a izquierda
Ejemplos:
● Oso
● "Sometamos o matemos"
● "Isaac no ronca así"
● Radar
● Ana
"""

texto_pedido = input("Ingrese un texto y veremos si es palindromo o no: ")

texto_minuscula = texto_pedido.lower # paso el texto completo a minusculas

texto_final = ""
for i in range (len(texto_minuscula)):
    texto_final += texto_pedido[-(i+1)]

print(texto_final)