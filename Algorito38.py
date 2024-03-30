from math import sin, radians
angulo = float(input("Digite os graus para calcular o Seno: "))
seno = sin(radians(angulo))
print(f"O Seno do ângulo {angulo} é {seno:.2f}")