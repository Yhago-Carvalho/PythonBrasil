'''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do retângulo, que deve ser um
objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo ponto que indique os valores
de x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''

from time import sleep
class Retangulo():
    def __init__(self):
        self.altura = float(input('Altura: '))
        self.largura = float(input('Largura: '))

    def centro(self):
        x = self.largura/2
        y = self.altura/2
        print(f'O centro do reângulo encontra-se nos pontos: \nx = {x} \ny = {y}')

class Ponto(Retangulo):
    def __init__(self):
        super().__init__()
        self.pontox = self.largura
        self.pontoy = self.altura
        self.x = self.pontox
        self.y = self.pontoy

    def inferorEsquerdo(self):
        self.x = 0
        self.y = 0
        print('O canto inferior esquerdo do reângulo encontra-se nos pontos: ')

    def inferiorDireito(self):
        self.x = self.pontox
        self.y = 0
        print('O canto inferior direito do reângulo encontra-se nos pontos: ')

    def superiorEsquerdo(self):
        self.x = 0
        self.y = self.pontoy
        print('O canto superior esquerdo do reângulo encontra-se nos pontos: ')

    def superiorDireito(self):
        self.x = self.pontox
        self.y = self.pontoy
        print('O canto supeior direito do reângulo encontra-se nos pontos: ')

    def imprimePontos(self):
        print(f'x = {self.x} \ny = {self.y}')

if __name__ == '__main__':
    while True:
        print('-'*40)
        print(f'{"MENU":^40}')
        print('-'*40)
        try:
            opc = int(input('''[1] Ver cantos do retângulo
[2] Ver centro do retângulo
[3] Sair
Digite sua opção: '''))
            while opc < 1 or opc > 3:
                opc = int(input('Digite uma opção válida: '))
            print('-' * 40)
        except:
            print('Você digitou um inteiro inválido, tente novamente!')
        else:
            if opc == 3:
                break
            else:
                ret = Ponto()
                if opc == 1:
                    ret.inferiorDireito()
                    ret.imprimePontos()
                    ret.inferorEsquerdo()
                    ret.imprimePontos()
                    ret.superiorDireito()
                    ret.imprimePontos()
                    ret.superiorEsquerdo()
                    ret.imprimePontos()
                else:
                    ret.centro()
            sleep(2)

