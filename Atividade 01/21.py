#Diferença entre dois números: Peça dois números e mostre a diferença absoluta entre eles (sem sinal negativo).

import os
clear = lambda: os.system('cls')


n1 = float(input("Informe primeiro numero: "))
n2 = float(input("Informe segundo numero: "))

resultado = n1/n2
   
print(f"O resultado da divisão e {resultado}")
