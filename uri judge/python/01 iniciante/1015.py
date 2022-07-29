linha_a = input('informe os eixos x e y do ponto A:\n').split(' ')
linha_b = input('informe os eixos x e y do ponto B:\n').split(' ')
x1 = float(linha_a[0])
y1 = float(linha_a[1])
x2 = float(linha_b[0])
y2 = float(linha_b[1])
dist = (((x2-x1)**2) + ((y2-y1)**2))**0.5
print ('{}'.format('%.4f'%dist))
