pw = input()
x = 0
while x < 1:
    if pw != str(2002):
        print ('Senha Invalida')
        pw = input()
    elif pw == str(2002):
        print ('Acesso Permitido')
        break
