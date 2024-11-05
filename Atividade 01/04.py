# Divisão de dois números: Peça ao usuário dois números e mostre o resultado da divisão do primeiro pelo segundo.
import os
clear = lambda: os.system('cls')

print("Informe dois números!")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o primeiro número: "))
resultado = n1/n2

clear()
print("------------------")
print("A divisão é: ", resultado)