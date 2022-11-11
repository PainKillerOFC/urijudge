cod_a = input('CÓDIGO DA PEÇA 1\n')
qnt_a = int(input('QUANTIDADE DE PEÇAS\n'))
vlr_a = float(input('VALOR DA PEÇA 1\n'))
cod_b = input('CÓDIGO DA PEÇA 2\n')
qnt_b = int(input('QUANTIDADE DE PEÇAS\n'))
vlr_b = float(input('VALOR DA PEÇA 2\n'))

total = (qnt_a*vlr_a)+(qnt_b*vlr_b)

print ('VALOR TOTAL A PAGAR: R$ {}'.format('%.2f'%total))
