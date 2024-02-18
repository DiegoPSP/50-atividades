def E_quadrado_perfeito(numero):
    if numero < 0:
        return False
    
    raiz_quadrada = int(numero ** 0.5)

    return raiz_quadrada ** 2 == numero
print("\n**Um quadrado perfeito é um número que pode ser expresso como o produto de um número por ele mesmo!**\n")

numero = int(input("Digite um valor: "))
if E_quadrado_perfeito(numero):
    print(f"{numero} é um quadrado perfeito.")
else:
    print(f"{numero} não é um quadrado perfeito.")
