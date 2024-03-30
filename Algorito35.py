print("***" * 20)
print("\nVamos analisar se o seu investimento será \33[0;32;40mrentável\33[m ou \33[0;31;40mnão\33[m!")

def calcular_vpl(fluxo_entrada, taxa_desconto, investimento):
    vpl = -investimento
    for t, fluxo in enumerate(fluxo_entrada):#enumerate faz com que vários parâmetros sejam iterados ao mesmo tempo(threads);
        vpl += fluxo / (1 + taxa_desconto) ** (t + 1)
    return vpl

investimento = float(input("Digite o valor de investimento: "))
taxa_desconto = 0.1
entradas = int(input("Digite quantos fluxos de entrada você planeja fazer: "))

fluxo_entrada = []
for i in range(entradas):
    fluxo = float(input(f"Digite qual o valor de cada entrada no caixa {i+1}: "))
    fluxo_entrada.append(fluxo)

resultado_vpl = calcular_vpl(fluxo_entrada, taxa_desconto, investimento)

if resultado_vpl < 0: 
    print(f"\nO investimento não é rentável pois o valor foi \33[0;31;40m R${resultado_vpl:.2f}\33[m!")
elif resultado_vpl == 0: 
    print(f"\nO investimento não terá lucro mas também não dará prejuízo pois o calculo ficou em \33[33m R${resultado_vpl:.2f}\33[m!")
else:
    print(f"\nO investimento trará o lucro de \33[0;32;40m R${resultado_vpl:.2f}\33[m!")

print("***" * 20)