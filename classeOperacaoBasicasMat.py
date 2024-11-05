import os
clear = lambda: os.system('cls')

class Operacao:
    def __init__(self, n1, acao, n2):
        self.n1 = n1
        self.acao = acao
        self.n2 = n2

    def calculo(self): 
        if self.acao == "+":
            print(f'{self.n1} + {self.n2} = {self.n1+self.n2}')
        elif self.acao == "-":
            print(f'{self.n1} - {self.n2} = {self.n1-self.n2}')
        elif self.acao == "*":
            print(f'{self.n1} * {self.n2} = {self.n1*self.n2}')
        else: 
            print(f'{self.n1} / {self.n2} = {self.n1/self.n2}')
            

calculadora = Operacao(float(input(f'Número 1: ')), input(f'Informe o operador + - * / '),float(input(f'Número 2: ')))

calculadora1 = Operacao(1, "+", 43)


clear()

calculadora.calculo()
calculadora1.calculo()
