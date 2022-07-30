# Leia o salário do funcionário e calcule e mostre o novo salário
# bem como o valor de reajuste ganho e o índice reajustado, em percentual.

#A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.
value = float(input())


if value <= 400:
    aum = 0.15
elif value <= 800:
    aum = 0.12
elif value <= 1200:
    aum = 0.1
elif value <= 2000:
    aum = 0.07
else:
    aum = 0.04
sal = value*aum + value
reaj = value*aum
perc = aum*100

sal = "%.2f"%(sal)
reaj = "%.2f"%(reaj)
perc = int(perc)

#Imprima 3 linhas na saída: 
# o novo salário:
print (f'Novo salario: {sal}')
# O valor ganho de reajuste
print (f"Reajuste ganho: {reaj}")
# o percentual de reajuste ganho
print (f"Em percentual: {perc} %")
