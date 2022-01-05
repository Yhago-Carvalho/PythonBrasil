'''
Classe Retangulo: Crie uma classe que modele um retangulo:

Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as medidades de um local. Depois,
deve criar um objeto com as medidas e calcular a quantidade de pisos e de rodapés necessárias para o local.
'''

class Retangulo():
    def __init__(self, comp, larg):
        self.comp = comp
        self.larg = larg

    def mudarLados(self):
        self.comp = float(input('Comprimento: '))
        self.larg = float(input('Largura: '))

    def retornaLados(self):
        print(f'O comprimento é {self.comp}m e a largura é {self.larg}m')

    def calcularArea(self):
        return self.larg * self.comp

    def calcularPerimetro(self):
        return self.larg * 2 + self.comp * 2


if __name__ == '__main__':
    retanulo = Retangulo(float(input('Comprimento: ')), float(input('Largura: ')))
    resp = input('Deseja mudar os valores? ').strip()[0]
    if resp in 'Ss':
        retanulo.mudarLados()
    retanulo.retornaLados()
    print(f'Serão necessário {retanulo.calcularArea()} m² de piso')
    print(f'Serão necessário {retanulo.calcularPerimetro()} metros de rodapé.')
