#  Área de um retângulo: Peça a largura e a altura de um retângulo e calcule a área.
import os
clear = lambda: os.system('cls')

print("Informe Largura e Altura de um retângulo.")
print("Informe a largura: ")
largura = float(input("Informe Largura: "))
print("Informe a Altura: ")
altura = float(input("Informe Altura: "))

resultado = largura * altura

clear() 
print("------------------")
print("O resultado da área do retângulo é: ", resultado)