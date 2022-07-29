value = float(input())
if value in range (-1, 401):
    aum = 0.15
elif value in range (401, 801):
    aum = 0.12
elif value in range (801, 1201):
    aum = 0.1
elif value in range (1201, 2001):
    aum = 0.07
else:
    aum = 0.04
sal = value*aum + value
print (f'Novo salario: {sal}\nReajuste ganho: {value*aum}\nEm percentual: {aum*100} %')
