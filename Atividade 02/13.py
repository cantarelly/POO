import os
clear = lambda: os.system('cls')

n1 = float(input("Informe o primeiro numero: "))
n2 = float(input("Informe o segundo numero: "))

clear()

if  n2 == 0:
    print(f'A divisão não é possível')
else:
    print(f'A divisão é {n1/n2}')
