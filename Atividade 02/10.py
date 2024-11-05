
import os
clear = lambda: os.system('cls')


nota = int(input("Informe uma nota de  0 a 10: "))

clear()

if  nota == 0  or nota <= 10:
    print(f'Nota válida! ')
else:
    print(f"Nota inválida!")
