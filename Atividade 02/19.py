import os
clear = lambda: os.system('cls')


idade = int(input("Informe sua idade: "))


clear()

if  idade >= 18:
    print(f'Pode dirigir!')
else:
    print(f"Ainda falta {18 - idade} anos para dirigir")
