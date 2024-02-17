a = int(input("Digite um numero inteiro para calcular o MMC:"))
b = int(input("Digite outro numero inteiro para calcular o MMC:"))
def mmc(a,b):
    mmc = a
    while mmc % b:
        mmc += a
    return mmc
print(mmc(a, b))