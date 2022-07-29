a, b, c = input().split(" ")
a = int(a)
b = int(b)
c = int(c)
#para o caso de A estar no meio
if a < b and a > c:
    print (c)
    print (a)
    print (b)
if a < c and a > b:
    print (b)
    print (a)
    print (c)
#para o caso de B estar no meio
if b < a and b > c:
    print (c)
    print (b)
    print (a)
if b < c and b > a:
    print (a)
    print (b)
    print (c)
#para o caso de C estar no meio
if c < a and c > b:
    print (b)
    print (c)
    print (a)
if c < b and c > a:
    print (a)
    print (c)
    print (b)
    
print ('')

print (a)
print (b)
print (c)
