# Como entrada, na primeira linha vai haver a descrição “Dia”,
# seguido de um espaço e o dia do mês no qual o evento vai começar
di = input("Dia ")
# Na linha seguinte, será informado o momento no qual o evento vai iniciar
# no formato hh : mm : ss
hi, mi, si = map(int, input().split(" : "))

# Na terceira e quarta linha de entrada haverá outra informação
# no mesmo formato das duas primeiras linhas, indicando o término do evento.

df = input("Dia ")
hf, mf, sf = map(int, input().split(" : "))

# ---------------- CALC ---------------- #

days = df - di
hours = hf - hi
minutes = mf - mi
seconds = sf - si

if df < di:
    days += 30
if hf < hi:
    hours += 24
    days -= 1
if mf < mi:
    minutes += 60
    hours -= 1
if sf < si:
    seconds += 60
    minutes -= 1



print (f"{days} dia(s)")
print (f"{hours} hora(s)")
print (f"{minutes} minuto(s)")
print (f"{seconds} segundo(s)")