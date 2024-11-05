#   Quantidade de segundos em um dia: Calcule quantos segundos existem em um dia (24 horas).

import os
clear = lambda: os.system('cls')

dia = int(input("Informe a quantidade de dias: "))


clear() 
print("------------------")
print(f"A conversão de dias({dia}) em segundos: {dia*24*60*60} dias")