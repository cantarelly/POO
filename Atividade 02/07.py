
import os
clear = lambda: os.system('cls')

n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
n3 = float(input("Informe a terceira nota: "))
media = (n1+n2+n3)/3
clear()

if  media >= 7:
    print(f'Aluno aprovado com a média {media: .2f}')
else:
    print(f"Aluno reprovado com a média {media: .2f}")
