#

import os
clear = lambda: os.system('cls')

idade = float(input("Informe sua idade: "))
clear()
if idade < 18:
    print("Você é menor de idade!")
else:
	print("Você é maior de idade!") 