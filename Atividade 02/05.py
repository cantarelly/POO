import os
clear = lambda: os.system('cls')

valor = float(input("Informe o valor da compra: "))
desconto = valor * 0.10

clear()
if valor <= 100:
    print(f"Você não teve um desconto de 10%")
    print(f"O valor da sua compra é {valor}")
else:
     print(f"Você teve um desconto de 10%")
     print(f"O valor do desconto é {desconto}")
     print(f"O valor a pagar é {valor-desconto}")