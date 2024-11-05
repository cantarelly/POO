import os
clear = lambda: os.system('cls')

ladoA = float(input("Informe o lado A do triângulo: "))
ladoB = float(input("Informe o lado B do triângulo:"))
ladoC = float(input("Informe o lado C do triângulo: "))

clear()

if  ladoA == ladoB:
    if ladoA == ladoC:
        print(f'triângulo equilátero')
    else:
        print(f'triângulo isósceles')
else:
    print(f'triângulo escaleno')
