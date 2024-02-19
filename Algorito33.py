def Converter_Binario(numero):
    if numero == 0:
        return 0
    binario = " "

    while numero > 0:
        resto = numero % 2
        binario = str(resto) + binario
        print(binario)
        numero//= 2

    return binario

numero = int(input('Digite um numero decimal: '))
resultado = Converter_Binario(numero)
print(f"****** O numero decimal {numero} convertido em binário é {resultado}******")
