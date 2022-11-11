# Faça um programa que leia 6 valores.
# Estes valores serão somente negativos ou positivos

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())
n6 = float(input())

n1 = round(n1)
n2 = round(n2)
n3 = round(n3)
n4 = round(n4)
n5 = round(n5)
n6 = round(n6)

value = 0

if n1 > 0:
    value += 1
if n2 > 0:
    value += 1
if n3 > 0:
    value += 1
if n4 > 0:
    value += 1
if n5 > 0:
    value += 1
if n6 > 0:
    value += 1
# A seguir, mostre a quantidade de valores positivos digitados.
print (f"{value} valores positivos")