'''
Classe Pessoa: Crie uma classe que modele uma pessoa:

Atributos: nome, idade, peso e altura
Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada ano que nossa pessoa envelhece,
sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

>>> YHAGO = Pessoa('Yhago Carvalho', 27, 98, 1.88)
>>> YHAGO.engordar()
99
>>> YHAGO.engordar()
100
>>> YHAGO.emagrecer()
99
>>> YHAGO.envelhecer()
28
>>> YHAGO.crecer()
1.93
>>> ADRIANO = Pessoa('Adriano Filho', 13, 60, 1.65)
>>> ADRIANO.envelhecer()
14
>>> ADRIANO.crecer()
1.75
'''

class Pessoa():
    def __init__(self, nome, idade = 21, peso = 75, altura = 1.70):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            Pessoa.crecer(self)
        self.idade += 1
        return self.idade

    def engordar(self):
        self.peso += 1
        return self.peso

    def emagrecer(self):
        self.peso -= 1
        return self.peso

    def crecer(self):
        self.altura += 0.05
        return self.altura