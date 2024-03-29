def amstrong(numero):
    valor = str(numero)
    potencia = len(valor)
    soma = 0
    for digito in valor:
        soma += int(digito) ** potencia
    if soma == numero:
        print(f"O número {numero} é um número de Amstrong!")
    else:
        print(f"O número {numero} é diferente de {soma}. Não é um número de Amstrong!")

numero = int(input("Digite um valor e veja se ele é um número de amstrong: "))
amstrong(numero)