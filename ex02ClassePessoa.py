import os
clear = lambda: os.system('cls')

class Pessoa:
    def __init__(self, nome, idade, cpf, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.endereco = endereco

    def preparaImpressa(self):
        print(f'nome: ',self.nome,'\nidade: ', self.idade, '\ncpf: ', self.cpf,'\nendereco: ', self.endereco)

persona = Pessoa(input('nome:'), input('idade:'), input('cpf:'), input('endereco:'))

clear()
persona.preparaImpressa()