a, b, c = input().split(' ')
a = float(a)
b = float(b)
c = float(c)
delt = b**2-4*a*c
if (2*a == 0) or (delt<0):
    print ('Impossivel calcular')
else:
    r1 = (-b + (delt**0.5)) /(2*a)
    r2 = (-b - (delt**0.5)) /(2*a)
    print ('R1 = {}'.format('%.5f'%r1))
    print ('R2 = {}'.format('%.5f'%r2))