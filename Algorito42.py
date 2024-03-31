def is_lucas_number(numero):
    if numero == 0:
        return True
    elif numero == 1:
        return True
    
    lucas_anterior, lucas_atual = 2, 1
    while lucas_atual < numero:
        lucas_proximo = lucas_anterior + lucas_atual
        lucas_anterior, lucas_atual = lucas_atual, lucas_proximo
        
    return lucas_atual == numero

numero = int(input("Digite um número para verificar se é um número de Lucas: "))
if is_lucas_number(numero):
    print(f"O número \33[0;32;40m{numero}\33[m É um número de Lucas!")
else:
    print(f"O número \33[0;31;40m{numero}\33[m NÃO é um número de Lucas!")
