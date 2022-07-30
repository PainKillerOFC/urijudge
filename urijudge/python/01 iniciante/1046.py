hi, mi, hf, mf = map(int, input().split(' '))
m = mf- mi
if mi > mf:
    m += 60
if hi >= hf:
    h = hf + (24-hi)
if hi < hf:
    h = hf - hi
if hi < hf and mi > mf:
    h -= 1
    m += 60
print (f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")