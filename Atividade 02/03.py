#
import os
clear = lambda: os.system('cls')

n1 = float(input("Informe o número: "))
clear()
if n1%2 == 0:
    print("A número informado é par! ")
else:
    print("A número informado é impar! ") 

    