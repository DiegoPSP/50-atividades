import random
palavra = str(input("Digite uma palavra e descubra se ela é anagrama de outra palavra: "))
anagrama = str(input("Agora digite a palavra para ser o anagrama da primeira: "))
print(list(palavra))
if len(list(palavra)) == len(list(anagrama)):
    aleatorio = random.sample(palavra, len(palavra))
    while list(aleatorio) != list(anagrama):
        aleatorio = random.sample(palavra, len(palavra))
else:
    print("Tamanhos diferentes! Não é um anagrama")

print(f"A palavra {list(palavra)} é um anagrama da palavra {list(anagrama)}!")


