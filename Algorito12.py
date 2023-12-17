numero = int(input("Digite um numero para saber o fatorial dele: "))
fatorial = 1
while numero > 1:
   fatorial *= numero
   numero -= 1 

print(f"O resultado é: {fatorial}")