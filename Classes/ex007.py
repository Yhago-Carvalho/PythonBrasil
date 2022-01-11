'''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):
Atributos: Nome, Fome, Saúde e Idade b. Métodos: Alterar Nome, Fome, Saúde e Idade; Retornar Nome, Fome, Saúde e Idade
Obs: Existe mais uma informação que devemos levar em consideração, o Humor do nosso tamagushi, este humor é uma combinação
entre os atributos Fome e Saúde, ou seja, um campo calculado, então não devemos criar um atributo para armazenar esta
informação por que ela pode ser calculada a qualquer momento.
>>> mascote = bichinhoVirtual('Princesa', 'sim', 75, 6)
>>> mascote.nomeBichinho()
'Princesa'
>>> mascote.fomeBichinho()
'sim'
>>> mascote.idadeBichinho()
6
>>> mascote.saudeBichinho()
75
'''

class bichinhoVirtual():
    def __init__(self, nome, fome = 'não', saude = 100, idade = 0):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterarNome(self):
        self.nome = input('Qual novo nome? ')
        return self.nome

    def nomeBichinho(self):
        return self.nome

    def fomeBichinho(self):
        return self.fome

    def saudeBichinho(self):
        return self.saude

    def idadeBichinho(self):
        return self.idade
