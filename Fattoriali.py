print("Inserisci numero da fattorializzare: ")
numero = input('-->')
num = int(numero)
def facto(n):
    fact = 1
    for x in range(1,int(n)):
        fact *= x+1

    return fact


fatt = []
for count in range(0,num):
    fatt.append(facto(count))

print(fatt)


