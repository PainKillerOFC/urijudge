cod, qnt = input('insira o código e a quantidade do item:\n').split(' ')
cod = int(cod)
qnt = int(qnt)
if cod == 1:
    price = 4
elif cod == 2:
    price = 4.5
elif cod == 3:
    price = 5
elif cod == 4:
    price = 2
elif cod == 5:
    price = 1.5
valor = price*qnt
print ('Total: R$ {}'.format('%.2f'%valor))
