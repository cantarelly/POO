import os
clear = lambda: os.system('cls')

print("Informe dois números!")
n1 = float(input("Informe o primeiro número: "))
n2 = float(input("Informe o segundo número: "))
clear()
if n1 > n2:
    print(f"O número {n1} é maior que o número {n2}")
else:
     print(f"O número {n2} é maior que o número {n1}")