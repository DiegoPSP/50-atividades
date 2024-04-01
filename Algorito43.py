def calcular_juros(valor, juros):
    juros = juros / 100
    valor = valor + (valor * juros)
    return valor
valor = float(input("Digite o capital inicial: "))
juros = float(input("Digite agora a taxa de juros(digite numeros inteiros. Conversão automática ativada!): "))
resultado = calcular_juros(valor, juros)
print(f"O valor R${valor:.2f} somado com a taxa de juros de {juros}% resulta em \33[0;32;40mR${resultado:.2f}\33[m!")