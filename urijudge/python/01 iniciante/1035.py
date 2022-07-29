a, b, c, d = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
d = int(d)

# se B for maior que C
valid = b > c

# se D for maior do que A
valid = valid and d>a

# a soma de C com D for maior que a soma de A e B
valid = valid and (c+d)>(a+b)

# se C e D, ambos, forem positivos
valid = valid and c>0 and d>0

# se a variável A for par
valid = valid and a%2 == 0

if valid:
    print ('Valores aceitos')
else:
    print ('Valores nao aceitos')