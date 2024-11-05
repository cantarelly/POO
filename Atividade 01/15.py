#  Cálculo de horas trabalhadas: Peça a quantidade de horas trabalhadas e o valor por hora, e calcule o salário total.
import os
clear = lambda: os.system('cls')

quantidade_horas = float(input("Informe a quantidade de horas trabalhadas: "))
valor_hora = float(input("Informe o valor da hora trabalhada: "))
salario_total = quantidade_horas * valor_hora

clear() 
print("------------------")
print("O salario total é: ", salario_total)