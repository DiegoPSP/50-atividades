def primos(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True
    
def quantidade_primos(num, final):
    proximo = num + 1
    count = 0
    while proximo <= final:
        if primos(proximo):
            count += 1
        proximo += 1
    return count


valor = int(input("Digite o inicio do intervalo de numeros: "))
final = int(input("Digite o final do intervalo de numeros: "))
resultado = quantidade_primos(valor, final)
print(f"\nExistem \33[0;32;40m{resultado}\33[m númemros primos dentre o intervalor fornecido!")