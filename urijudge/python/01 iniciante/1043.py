# Leia 3 valores reais (A, B e C)
a, b, c = input().split(" ")
a = float(a)
b = float(b)
c = float(c)

perimetro = a+b+c
area = ((a+b)*c)/2
# verifique se eles formam ou não um triângulo
# Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
if a<(b+c) and b<(a+c) and c<(b+a):
    perimetro = "%.1f"%(perimetro)
    print(f"Perimetro = {perimetro}")

# Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura
else:
    area = "%.1f"%(area)
    print(f"Area = {area}")