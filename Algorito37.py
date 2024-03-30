def numero_primo(valor):
    if valor <= 1:
        return False
    for i in range(2, int(valor ** 0.5) + 1):
        if valor % i == 0:
            return False        
    return True
       
def proximo_primo(num):
    proximo = num + 1
    while True:
        if numero_primo(proximo):
            return proximo
        proximo += 1

numero = int(input("Digite um número e veja se ele é primo: "))
resultado = proximo_primo(numero)
print(f"\nO próximo número primo depois de {numero} é \33[0;32;40m{resultado}\33[m!\n")