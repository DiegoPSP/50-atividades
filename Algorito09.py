palavra = str(input("Digite uma palavra e confirme se ela é ou não um palíndromo:"))
if palavra == palavra[::-1]:
    print(f'A palavra {palavra.upper()} é um palíndromo')
else:
    print('Não é um palíndromo')