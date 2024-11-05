import os
clear = lambda: os.system('cls')


idade = int(input("Informe sua idade: "))

clear()

if  idade < 12 :
    print(f'Criança ')
elif idade < 18 :
    print(f"Adolescente!")
else:
    print('Adulto')