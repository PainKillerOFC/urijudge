#Faça um programa que leia 5 valores inteiros.

n1 = float(input())
n2 = float(input())
n3 = float(input())
n4 = float(input())
n5 = float(input())



value = 0

if n1 % 2 == 0:
    value += 1
if n2 % 2 == 0:
    value += 1
if n3 % 2 == 0:
    value += 1
if n4 % 2 == 0:
    value += 1
if n5 % 2 == 0:
    value += 1

print (f"{value} valores pares")