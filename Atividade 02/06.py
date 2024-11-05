#VERIFICAR SE O NUMERO DIGITADO E MULTIPLO DE 5
import os
clear = lambda: os.system('cls')

n1 = int(input("Informe o número: "))
clear()
if n1%5 == 0:
    print(f"A número {n1} informado é multiplo de 5! ")
else:
    print(f"A número {n1} informado não é multiplo de 5! ") 
