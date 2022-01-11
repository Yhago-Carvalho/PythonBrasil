'''
Classe Macaco: Desenvolva uma classe Macaco,que possua os atributos nome e bucho (estomago) e pelo menos os métodos
comer(), verBucho() e digerir(). Faça um programa ou teste interativamente, criando pelo menos dois macacos, alimentando-os
com pelo menos 3 alimentos diferentes e verificando o conteúdo do estomago a cada refeição. Experimente fazer com que um
macaco coma o outro. É possível criar um macaco canibal?
'''

class Macaco():
    def __init__(self, nome, bucho=50):
        self.nome = nome
        self.bucho = bucho
        self.situação = 'Quero comida'

    def comer(self, alimento=0):

        try:
            self.bucho += int(alimento)
        except:
            self.bucho = 100

        if self.bucho >= 100:
            self.bucho = 100
        elif self.bucho < 0:
            self.bucho = 0

    def digerir(self):
        self.bucho -= 30

    def verBucho(self):
        if self.bucho == 100:
            self.situação = 'Estou muito cheio'
        elif self.bucho >= 70:
            self.situação = 'Estou satisfeito'
        else:
            self.situação = 'Quero comida'
        print(self.situação)

if __name__ == '__main__':
    banana_ana = 20
    banana_prata = 15
    banana_comprida = 25
    banana_nanica = 10

    orangotango = Macaco('orangotango')
    orangotango.verBucho()
    orangotango.comer(banana_comprida)
    orangotango.comer(banana_prata)
    orangotango.verBucho()
    orangotango.digerir()
    orangotango.comer(banana_comprida)
    orangotango.comer(banana_ana)
    orangotango.comer(banana_nanica)
    orangotango.verBucho()

    gorila = Macaco('Gorila', 0)
    gorila.verBucho()
    gorila.comer(orangotango)
    gorila.verBucho()