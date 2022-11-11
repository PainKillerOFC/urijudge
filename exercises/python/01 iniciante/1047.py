# Leia
# hora inicial, minuto inicial, hora final e minuto final de um jogo
hi, mi, hf, mf = input().split(' ')
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)


# calcule a duração do jogo
h = hf - hi
m = mf - mi

if m < 0:
    h -= 1
    m += 60
if hf == hi and mf == mi or hi > hf:
    h += 24
    
print (f'O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)')