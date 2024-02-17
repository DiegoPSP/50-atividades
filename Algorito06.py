numero = int(input("Digite um número e saiba se ele é primo: "))
contador = 0
for c in range (1, numero + 1):
    if numero % c == 0:
        print('\033[33m', end=' ')
        contador += 1
    else:
        print('\033[31m', end=' ')
    print(f"{c}", end=' ')
print(f"\n\033[mO numero {numero} foi divisível {contador} vezes")
if contador == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
