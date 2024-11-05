import os
clear = lambda: os.system('cls')


media = float(input("Informe a média do aluno: "))

clear()

if  media >= 7 :
    print(f'Aprovado')
elif media >= 5 and media < 7 :
    print(f"Recuperação!")
else:
    print('Reprovado')