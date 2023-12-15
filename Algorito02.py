vetor_Divisão_inteira = [1, 3, 5, 7, 11, 13, 17, 19]
vetor_Primos = [0, 2, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]

print("---------ANTES------------")
print(vetor_Divisão_inteira)
print(vetor_Primos)
print("--------------------------")

aux = vetor_Divisão_inteira
vetor_Divisão_inteira = vetor_Primos
vetor_Primos = aux

print("---------DEPOIS-----------")
print(vetor_Divisão_inteira)
print(vetor_Primos)
print("--------------------------")
