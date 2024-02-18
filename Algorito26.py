import re #Biblioteca de Expressões Regulares;
print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
print("* caracter obrigatório.\n")
senha = str(input("Digite sua senha: "))#"While not" fica em um loop até todas as especificações forem verdadeiras;
while not (re.search(r'.{8,}', senha) and #Faz uma busca na string, verificando se ela contém 8 caracteres no mínimo;
           re.search(r'.*[A-Z]', senha) and #Verifica se a string contém ao menos uma letra MAIÚSCULA;
           re.search(r'\d', senha) and #Verifica se a string contém ao menos um número;
           re.search(r'[!@#$%¨&*]', senha)):#...ao menos um desses caracteres especiais;
    senha = str(input("Digite uma senha que inclua todos os critérios: "))

print("Senha cadastrada com sucesso")
