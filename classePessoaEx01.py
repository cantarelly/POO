import os
clear = lambda: os.system('cls')

class Pessoa:
    def __init__(self, nome, sobrenome, idade, cidade):
       self.nome = nome
       self.sobrenome = sobrenome
       self.idade = idade
       self.cidade = cidade
    
    def preparaImpressao(self):
        print("-------------Saída de Dados-------------")
        print(f'Nome: ',self.nome,'\nSobrenome: ',self.sobrenome,'\nIdade: ',self.idade,'\nCidade: ',self.cidade,)



usuario1 = Pessoa(input("Nome: "), input("Sobrenome: "), input("Idade: "), input("Cidade: "))

clear()
usuario1.preparaImpressao()