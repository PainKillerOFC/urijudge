# Neste problema, você deverá ler 3 palavras
word_one = str(input())
word_two = str(input())
word_thr = str(input())

if word_one == str("vertebrado"):
    if word_two == str("ave"):
        if word_thr == str("carnivoro"):
            print ("aguia")
        else:
            print ("pomba")
    else:
        if word_thr == str("onivoro"):
            print ("homem")
        else:
            print ("vaca")
else:
    if word_two == str("inseto"):
        if word_thr == str("hematofago"):
            print ("pulga")
        else:
            print ("lagarta")
    else:
        if word_thr == str("hematofago"):
            print ("sanguessuga")
        else:
            print ("minhoca")