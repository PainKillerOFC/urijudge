tt = int(input())
cem = tt//100
restcem = tt%100
cinq = restcem//50
restcinq = restcem%50
vinte = restcinq//20
restvinte = restcinq%20
dez = restvinte//10
restdez = restvinte%10
cinc = restdez//5
restcinc = restdez%5
dois = restcinc//2
restdois = restcinc%2
um = restdois//1
print (tt)
print ('{} nota (s) de R$ 100,00'.format(cem))
print ('{} nota (s) de R$ 50,00'.format(cinq))
print ('{} nota (s) de R$ 20,00'.format(vinte))
print ('{} nota (s) de R$ 10,20'.format(dez))
print ('{} nota (s) de R$ 5,00'.format(cinc))
print ('{} nota (s) de R$ 2,00'.format(dois))
print ('{} nota (s) de R$ 1,00'.format(um))
