# Conversão de temperatura: Converta uma temperatura em graus Celsius para
# Fahrenheit usando a fórmula: ---F = C x 1,8 + 32.
import os
clear = lambda: os.system('cls')

print("Informe uma temperatura em graus Celsius: ")
temperatura = float(input("Informe a temperatura: "))

fahrenheit = (temperatura * 1.8) + 32

clear() 
print("------------------")
print("O resultado da conversão para Fahrenheit é: ", fahrenheit)