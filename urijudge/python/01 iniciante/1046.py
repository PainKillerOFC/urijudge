hi, hf = input().split(' ')
hi = int(hi)
hf = int(hf)
if hi >= hf:
    h = hf + (24-hi)
    print (f'O JOGO DUROU {h} HORA(S)')
elif hi < hf:
    h = hf - hi
    print (f'O JOGO DUROU {h} HORA(S)')
