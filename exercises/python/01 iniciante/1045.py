# Leia 3 valores de ponto flutuante A, B e C
# ordene-os em ordem decrescente, de modo que
# o lado A representa o maior dos 3 lados
a, b, c = sorted(list(map(float, input().split(" "))), reverse= True)

# A seguir, determine o tipo de triângulo
# que estes três lados formam
# se A ≥ B+C, apresente a mensagem: NAO FORMA TRIANGULO
if a >= b+c:
    print("NAO FORMA TRIANGULO")
# se A**2 = B**2 + C**2, apresente a mensagem: TRIANGULO RETANGULO
elif a**2 == (b**2 + c**2):
    print("TRIANGULO RETANGULO")
# se A**2 > B2 + C**2, apresente a mensagem: TRIANGULO OBTUSANGULO
elif a**2 > (b**2 + c**2):
    print("TRIANGULO OBTUSANGULO")
# se A**2 < B2 + C**2, apresente a mensagem: TRIANGULO ACUTANGULO
elif a**2 < (b**2 + c**2):
    print("TRIANGULO ACUTANGULO")
# se os três lados forem iguais, apresente a mensagem: TRIANGULO EQUILATERO
if a == b == c:
    print("TRIANGULO EQUILATERO")
# se apenas dois dos lados forem iguais, apresente a mensagem: TRIANGULO ISOSCELES
elif a == b or b == c:
    print("TRIANGULO ISOSCELES")