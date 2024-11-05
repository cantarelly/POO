#

import os
clear = lambda: os.system('cls')

n1 = float(input("Informe o número: "))
clear()
if n1 < 0:
    print("A número informado é negativo! ")
elif n1 > 0:
    print("A número informado é positivo! ") 
else:
	print("A número informado é Zero! ") 
    