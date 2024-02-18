import re
print("Cadastre aqui sua senha com os seguintes critérios: \n"
      "         *Ao menos 8 digitos\n"
      "         *Ao menos uma letra MAIÚSCULA\n"
      "         *Ao menos um número\n"
      "         *Ao menos um caractere especial(!@#$%¨&*)\n")
print("* caracter obrigatório.\n")
senha = str(input("Digite sua senha: "))
while not (re.search(r'.{8,}', senha) and 
           re.search(r'.*[A-Z]', senha) and 
           re.search(r'\d', senha) and 
           re.search(r'[!@#$%¨&*]', senha)):
    senha = str(input("Digite uma senha que inclua todos os critérios: "))

print("Senha cadastrada com sucesso")
