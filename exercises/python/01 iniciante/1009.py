nome = input('NOME DO FUNCIONÁRIO\n')
fix = float(input('SALÁRIO FIXO\n'))
vendas = float(input('VENDAS EFETUADAS NO MÊS\n'))
salary = (vendas*0.15+fix)
salary_ = '%.2f'%salary
print ('')
print ('O SALARIO DE {} É DE R$ {}'.format(nome, salary_))
