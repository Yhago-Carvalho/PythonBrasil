'''
Classe Bola: Crie uma classe que modele uma bola:
Atributos: Cor, circunferência, material
Métodos: trocaCor e mostraCor
>>> bola = Bola()
>>> bola.mostraCor()
Vermelho
>>> bola.trocaCor(AMARELO)
>>> bola.mostraCor()
Amarelo
>>> bola.trocaCor(BRANCO)
>>> bola.mostraCor()
Branco
'''
VERMELHO = 'Vermelho'
AMARELO = 'Amarelo'
AZUL = 'Azul'
PRETO = 'Preto'
BRANCO = 'Branco'

class Bola():
    def __init__(self):
        self.cor = VERMELHO
        self.circ = 20
        self.material = 'Couro'

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        print(self.cor)
