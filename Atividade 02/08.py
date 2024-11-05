
import os
clear = lambda: os.system('cls')


senha = (input("Informe a senha para entrar no sistema: "))

clear()

if  senha == 'python123_EFG':
    print(f'Acesso permitido! ')
else:
    print(f"Acesso negado!")
