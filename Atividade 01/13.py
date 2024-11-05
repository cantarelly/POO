#  Área de um círculo: Peça o raio de um círculo e calcule a área usando a fórmula:
import os
clear = lambda: os.system('cls')

pi = float(3.1415)

print("Calcular área de um circulo.")
raio = float(input("Informe o raio: "))

resultado = pi * (raio**2)

clear() 
print("------------------")
print("O resultado da área do circulo é: ", resultado)