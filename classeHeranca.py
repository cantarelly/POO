class Animal:
    def __init__(self, nomee, idadee):
        self.nome = nomee
        self.idade = idadee
def falar(self):
    print(f'O {self.nome} esta falando.')


class Cachorro:
    def __init__(self, nomee, idadee, raca):
        super().__init__(nomee, idadee)
        self.raca = raca
def latir(self):
    print(f'O {self.nome} esta latindo!')

meu_cachorro = Cachorro("Zeus", 21, "Vira Lata")

print(meu_cachorro.raca)
#print(f'{meu_cachorro.nome, meu_cachorro.idade, meu_cachorro.raca}')