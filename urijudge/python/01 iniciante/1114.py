password = input()
while True:
    if password == str(2002):
        print ('Acesso Permitido')
        break
    else:
        print ('Senha Invalida')
        password = input()
