import math

def calcular_cosseno_graus(angulo_graus):
    # Converter graus para radianos
    angulo_radianos = math.radians(angulo_graus)
    
    # Calcular o cosseno do ângulo em radianos
    cosseno = math.cos(angulo_radianos)
    
    return cosseno

# Exemplo de uso:
angulo_graus = 60
cosseno_resultado = calcular_cosseno_graus(angulo_graus)
print("O cosseno de {:.2f} graus é aproximadamente {:.2f}".format(angulo_graus,cosseno_resultado))
