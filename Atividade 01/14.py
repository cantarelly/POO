#  Conversão de metros para centímetros: Peça um valor em metros e converta para centímetros.
import os
clear = lambda: os.system('cls')

metros = float(input("Informe o valor em metros: "))

resultado = metros * 100

clear() 
print("------------------")
print("O resultado da conversão para centimetros é: ", resultado, "centimetros.")