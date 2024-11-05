import os
clear = lambda: os.system('cls')

class Carro:
    def __init__(self, marca, ano, cor):
        self.marca = marca
        self.ano = ano
        self.cor = cor

    def preparaImpressa(self):
        print(f'Marca: ',self.marca,'\nAno: ', self.ano, '\nCor: ', self.cor)

car = Carro(input('Marca:'), input('Ano:'), input('Cor:'))

clear()
car.preparaImpressa()