def calcular_compostos(capital_inicial, tempo, taxa):
    juros = capital_inicial * (1 + taxa) ** tempo
    return juros
print("***" * 20)
capital_inicial = float(input("Digite o valor inicial do investimento: "))
tempo = int(input("Digite por quanto tempo você deseja investir(meses): "))
taxa = 0.01
final = calcular_compostos(capital_inicial, tempo, taxa)

print(f"\nO montante final será de \33[0;32;40mR${final:.2f}\33[m!\n")
print("***" * 20)