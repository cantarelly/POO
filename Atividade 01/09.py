# Conversão de moeda: Peça um valor em reais e mostre o valor convertido em dólares. Considere uma taxa de conversão fixa
import os
clear = lambda: os.system('cls')

valor_dolar =float(5.50)
print("Informe um valor em reais para converter em dólares: ")
valor = float(input("Informe o valor em reais: "))

resultado = valor * valor_dolar

clear() 
print("------------------")
print("O resultado da conversão para Dólar é: ", resultado)