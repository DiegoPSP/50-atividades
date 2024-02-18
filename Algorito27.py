from datetime import datetime
print("************Calculadora de Dias**************\n")
dias_inicial = int(input("Digite o dia inicial: "))
mes_inicial = int(input("Digite o mês inicial: "))
ano_inicial = int(input("Digite o ano inicial: "))
print()
dias_final = int(input("Digite agora o dia final: "))
mes_final = int(input("Digite agora o mês final: "))
ano_final = int(input("Digite agora o ano final: "))
print("*********************************************\n")
def Calcular_diferenca(dias_inicial,mes_inicial,ano_inicial, dias_final, mes_final, ano_final):
    data_inicial = datetime(year=ano_inicial, month=mes_inicial, day=dias_inicial)
    data_final = datetime(year=ano_final, month=mes_final, day=dias_final)
    diferenca_de_Dias = data_final - data_inicial
    return diferenca_de_Dias.days

print("A diferença de dias entre as datas é: "
     f" {Calcular_diferenca(dias_inicial, mes_inicial,ano_inicial, dias_final, mes_final, ano_final)} dias.")