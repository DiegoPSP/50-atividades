celsius = float(input("Digite a temperatura em graus Celsius: "))

def Converter_Celsius(celsius):
    fahrenheit = 32 + (celsius * 1.8)
    return fahrenheit

print("A temperatura {:.2f}ºC convertida em Fahrenheit é {:.2f}".format(celsius, Converter_Celsius(celsius)))