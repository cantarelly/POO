import os
clear = lambda: os.system('cls')


peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua altura: "))

imc = peso / (altura*altura)

clear()

if  imc >= 25 :
    print(f'Acima do Peso')
elif imc >= 18.5 or imc < 25 :
    print(f"Peso normal!")
else:
    print('Abaixo do peso')