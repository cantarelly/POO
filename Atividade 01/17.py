#  Calcular a velocidade média: Peça a distância percorrida e o tempo gasto, e calcule a velocidade média usando a fórmula:
import os
clear = lambda: os.system('cls')

distancia = float(input("Informe o valor da distancia: "))
tempo = float(input("Informe o tempo percorrido: "))
velocidade_media = distancia/tempo

clear() 
print("------------------")
print("A velocidade média é ", velocidade_media)