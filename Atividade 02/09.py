
import os
clear = lambda: os.system('cls')


idade = int(input("Informe sua idade: "))

clear()

if  idade <= 5  or idade >= 60:
    print(f'Entrada gratuita! ')
else:
    print(f"Comprar ingresso!")
