numero = int(input("Digite um número: "))
limite = int(input("Digite o limite do multiplicador número: "))
def tabela_multiplicacao(numero, limite):
    print(f"\nTabela de Multiplicação do {numero} até {limite}:\n")
    for i in range(0, limite + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

tabela_multiplicacao(numero, limite)


    