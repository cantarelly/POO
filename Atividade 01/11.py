#  Perímetro de um quadrado: Peça o lado de um quadrado e calcule o perímetro (soma dos lados).
import os
clear = lambda: os.system('cls')

print("Informe o lado de um quadrado.")
lado = float(input("Informe Largura: "))


resultado = lado * 4

clear() 
print("------------------")
print("O resultado do perímetro do quadrado é: ", resultado)