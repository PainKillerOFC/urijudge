hi, mi, hf, mf = input().split(' ')
hi = int(hi)
mi = int(mi)
hf = int(hf)
mf = int(mf)
hour = hf - hi
if hour < 0:
    hour += 24
mnt = mf - mi
if mnt < 0:
    mnt += 60
    hour -= 1
if hf == hi and mf == mi:
    print (f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print (f'O JOGO DUROU {hour} HORA(S) E {mnt} MINUTO(S)')
