'''
Classe Quadrado: Crie uma classe que modele um quadrado:

Atributos: Tamanho do lado
Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;
>>> quadrado = Quadrado()
>>> quadrado.retornaLado()
4
>>> quadrado.mudarLado(3)
>>> quadrado.retornaLado()
3
>>> quadrado.calcularArea()
9
'''

class Quadrado():
    def __init__(self):
        self.lado = 4

    def retornaLado(self):
        print(self.lado)

    def mudarLado(self, novo_lado):
        self.lado = novo_lado

    def calcularArea(self):
        return self.lado ** 2