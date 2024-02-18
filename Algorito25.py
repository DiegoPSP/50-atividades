import math
cateto_Adjacente = 12
cateto_Oposto = 16

def Calcular_Hipotenusa(cateto_Adjacente,cateto_Oposto):
    hipotenusa = (cateto_Adjacente**2) + (cateto_Oposto**2)
    return hipotenusa

print(math.sqrt(Calcular_Hipotenusa(cateto_Adjacente, cateto_Oposto)))