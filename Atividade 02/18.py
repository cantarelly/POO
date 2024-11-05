import os
clear = lambda: os.system('cls')


usuario = (input("Informe o login: "))
senha = (input("Informe a senha para entrar no sistema: "))

clear()

if  senha == '1234' and usuario == 'admin':
    print(f'Login bem sucedido ')
else:
    print(f"Acesso negado!")
