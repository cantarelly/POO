# Potência de um número: Peça um número e um expoente, e mostre o resultado do número elevado a esse expoente.
import os
clear = lambda: os.system('cls')

print("Informe dois números!")

numero = int(input("Informe o número: "))
expoente = int(input("Informe o expoente: "))
resultado = numero**expoente

clear() 
print("------------------")
print("O resultado da pontência é: ", resultado)