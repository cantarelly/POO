# Média de três números: Peça três números e mostre a média deles.
import os
clear = lambda: os.system('cls')

print("Informe três números para calcular a média entre eles")
numero1 = float(input("Informe o número: "))
numero2 = float(input("Informe o número: "))
numero3 = float(input("Informe o número: "))
media = (numero1+numero2+numero3)/3

clear() 
print("------------------")
print("O resultado da média é: ", media)