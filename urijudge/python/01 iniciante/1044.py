a = input()
b = input()
a = int(a)
b = int(b)
c = 1
if a < b:
    for c in range (c, b+2):
        if a*c == b:
            print ('Sao multiplos')
            break
        elif a*c != b:
            c += 1
            if a*c > b:
                print ('Nao sao multiplos')
                break
if b < a:
    for c in range (c, a+2):
        if b*c == a:
            print ('Sao multiplos')
            break
        elif b*c != a:
            c += 1
            if b*c > a:
                print ('Nao sao multiplos')
                break
