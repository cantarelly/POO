#  Preço com desconto: Peça o preço de um produto e o percentual de desconto, e mostre o preço final com desconto aplicado.
import os
clear = lambda: os.system('cls')

valor_produto = float(input("Informe o valor do produto: "))
percentual_desconto = float(input("Informe o percentual do desconto: "))
preco_final = valor_produto - (valor_produto * percentual_desconto/100)

clear() 
print("------------------")
print("O valor do produto com desconto aplicado é: ", preco_final)