import os
clear = lambda: os.system('cls')



class contaBancaria:
    def __init__(self, cliente, deposito):
       self.cliente = cliente
       self.deposito = float(deposito)

    def depositar(self):
        saldo = float(1000)
        print(f'Saldo anterior: ',saldo)
        saldo = saldo + self.deposito
        print(f'Valor depositado: ',self.deposito)
        print(f'Cliente: ', self.cliente, 'Saldo Atual: ', saldo)


cliente = contaBancaria(input('Para qual cliente deseja depositar: '), input('Valor a ser depositado: '))

clear()
cliente.depositar()