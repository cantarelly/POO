import os
clear = lambda: os.system('cls')

n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))
n3 = float(input("Informe o terceiro numero: "))

clear()

if  n1 > n2:
    if n1 > n3:
        print(f'O número maior é {n1}')
    else:
        print(f'O número maior é {n3}')
else:
    if n2 > n3:
        print(f'O número maior é {n2}')
    else:
        print(f'O número maior é {n3}')
