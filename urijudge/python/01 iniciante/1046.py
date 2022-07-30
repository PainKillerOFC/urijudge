hi, mi, hf, mf = map(int, input().split(' '))
mi += hi*60
mf += hf*60
m = mf-mi
if m <= 0:
    m += 24*60
h = m//60
m = m%60
print (f"O JOGO DUROU {h} HORA(S) E {m} MINUTO(S)")