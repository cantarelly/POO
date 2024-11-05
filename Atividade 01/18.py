#  Converter idade em dias: Peça a idade de uma pessoa em anos e converta para dias. Desconsidere anos bissextos.
import os
clear = lambda: os.system('cls')

idade = int(input("Informe sua idade: "))


clear() 
print("------------------")
print(f"A conversão da idade({idade}) em dias: {idade*365} dias")