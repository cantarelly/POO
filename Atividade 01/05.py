# Resto da divisão: Peça dois números inteiros e mostre o resto da divisão entre eles.
import os
clear = lambda: os.system('cls')

print("Informe dois números!")
n1 = int(input("Informe o primeiro número: "))
n2 = int(input("Informe o primeiro número: "))
resultado = n1%n2

clear()
print("------------------")
print("O resto é: ", resultado)