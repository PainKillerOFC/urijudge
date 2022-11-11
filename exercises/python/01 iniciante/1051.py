# Leia um valor com duas casas decimais
sal = float(input())

# Em seguida, calcule e mostre o valor que 
# esta pessoa deve pagar de Imposto de Renda

value = sal
if sal >= 2000.01 and sal <= 3000:
    value = sal - 2000
    taxa = 8/100*value
    taxa = "%.2f"%taxa
    print (f"R$ {taxa}")

elif sal >= 3000.01 and sal <= 4500:
    taxa = 8/100*1000
    value = sal - 3000
    taxa += 18/100*value
    taxa = "%.2f"%taxa
    print (f"R$ {taxa}")
elif sal > 4500:
    taxa = 8/100*1000
    taxa += 18/100*1500
    value = sal - 4500
    taxa += 28/100*value
    taxa = "%.2f"%taxa
    print (f"R$ {taxa}")
else:
    print ("Isento")