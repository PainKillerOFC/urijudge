dias = int(input('dias:\n'))
anos = dias//365
meses = (dias%365)//30
days = dias-(anos*365+(meses*30))
print ('{} ano (s)\n{} mes (es)\n{} dia(s)'.format(anos, meses, days))
