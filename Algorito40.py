def calcular_area(base, altura):
    area = (base * altura)/2
    return area

base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))
resultado = calcular_area(base, altura)
print(f"A área de um triângulo com base \33[0;33;40m{base:.2f}\33[m e altura \33[0;33;40m{altura:.2f}\33[m é \33[0;32;40m{resultado:.2f}\33[mcm²!")
