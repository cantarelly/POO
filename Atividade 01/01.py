# Soma de dois números: Peça ao usuário dois números e mostre a soma deles
import os
clear = lambda: os.system('cls')

print("Informe dois números!")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o primeiro número: "))
soma = n1+n2

clear()
print("------------------")
print("A soma é: ", soma)