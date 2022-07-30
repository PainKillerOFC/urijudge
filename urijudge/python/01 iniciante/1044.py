a, b = input().split(" ")
a = int(a)
b = int(b)
c = 1
if a < b:
    for c in range (c, b+2):
        if a*c == b:
            print ('Sao Multiplos')
            break
        elif a*c != b:
            c += 1
            if a*c > b:
                print ('Nao sao Multiplos')
                break
if b < a:
    for c in range (c, a+2):
        if b*c == a:
            print ('Sao Multiplos')
            break
        elif b*c != a:
            c += 1
            if b*c > a:
                print ('Nao sao Multiplos')
                break
