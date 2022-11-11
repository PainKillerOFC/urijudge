nota_a = float(input())
nota_b = float(input())
peso_a = (nota_a/10)*3.5
peso_b = (nota_b/10)*7.5
nota_peso = peso_a + peso_b
nota_final = (nota_peso*10)/11
nota_final = round(nota_final,5)
print ('')
print ('MÉDIA = {}'.format('%.5f'%(nota_final)))
