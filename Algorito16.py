fibonati = 0
segundo = 1
terceiro = 0
lista = []

stop = int(input("Digite até qual valor de fibonati você deseja saber: "))

if stop == 1:
    lista.append(fibonati)
    print(lista)
elif stop == 2:
    lista.append(fibonati)
    lista.append(segundo)
    print(lista)
else:
    lista.append(fibonati)
    lista.append(segundo)
    while len(lista) != stop:
        terceiro = fibonati + segundo
        fibonati = segundo
        segundo = terceiro
        lista.append(terceiro)

print(list(lista))

