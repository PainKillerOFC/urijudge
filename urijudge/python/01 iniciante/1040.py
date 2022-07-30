# Leia quatro números (N1, N2, N3, N4)
n1, n2, n3, n4 = input().split(' ')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
n4 = float(n4)

# Calcule a média com pesos 2, 3, 4 e 1
md = (n1*2 + n2*3 + n3*4 + n4)/10
media = "%.1f"%(md)


# Mostre esta média acompanhada pela mensagem "Media: "
# Se esta média for maior ou igual a 7.0,
# imprima a mensagem "Aluno aprovado."
if md >= 7:
    print (f"Media: {media}")
    print ("Aluno aprovado.")

# Se a média calculada for inferior a 5.0,
# imprima a mensagem "Aluno reprovado."
elif md < 5:
    print (f"Media: {media}")
    print ("Aluno reprovado.")

# Se a média calculada for um valor entre 5.0 e 6.9,
# o programa deve imprimir a mensagem "Aluno em exame.".
if md >= 5 and md <= 6.9:
    print (f"Media: {media}")
    print ("Aluno em exame.")

    #No caso do aluno estar em exame, leia um valor
    # correspondente à nota do exame obtida pelo aluno.
    exame = float(input())
    ex = "%.1f"%(exame)

    # (some a pontuação do exame com a média anteriormente calculada e divida por 2)
    print(f"Nota do exame: {ex}")
    mediafinal = (exame+md)/2
    mf = "%.1f"%(mediafinal)

# imprima a mensagem "Aluno aprovado." (caso a média final seja 5.0 ou mais )
    if mediafinal >= 5:
        print ("Aluno aprovado.")
        print (f"Media final: {mf}")

# "Aluno reprovado.", (caso a média tenha ficado 4.9 ou menos)
    else:
        print("Aluno reprovado.")
        print (f"Media final: {mf}")