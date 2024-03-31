def fibonacci(numero):
    sequencia = [0, 1]
    if numero == 0:
        return [0]
    elif numero == 1:
        return [1]
    else:
        while len(sequencia) < numero:
            proximo = sequencia[-1] + sequencia [-2]
            sequencia.append(proximo)
        return sequencia

numero = int(input("Digite o número para saber o fibonacci: "))
resultado = fibonacci(numero)
print(f"O número Fibonacci que você deseja é {resultado[-1]}")