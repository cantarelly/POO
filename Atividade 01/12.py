#  Área de um triângulo: Peça a base e a altura de um triângulo e calcule a área usando a fórmula: area = (base x altura) / 2
import os
clear = lambda: os.system('cls')

print("Calcular área de um triângulo.")
base = float(input("Informe base: "))
altura = float(input("Informe base: "))

resultado = (base * altura) / 2

clear() 
print("------------------")
print("O resultado da área do triângulo é: ", resultado)