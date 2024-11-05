import os
clear = lambda: os.system('cls')

n1 = float(input("Informe o numero: "))


clear()

if  n1 >= 10 and n1 <= 50:
    print(f'O numero digitado esta entre 10 e 50')
else:
    print(f'O número digitado não esta entre 10 e 50')
