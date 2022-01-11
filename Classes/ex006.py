'''
Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O usuário deve ser capaz de informar o
número do canal e aumentar ou diminuir o volume. Certifique-se de que o número do canal e o nível do volume permanecem
dentro de faixas válidas.
>>> tv = TV(1, 100)
>>> tv.aumentarVolume()
>>> tv.mostrarVolume()
100
>>> tv.diminuirVolume()
>>> tv.mostrarVolume()
99
'''

class TV():
    def __init__(self, canal=1, volume=0):
        if canal < 1:
            self.canal = 1
        elif canal > 45:
            self.canal = 45
        else:
            self.canal = canal
        if volume > 100:
            self.volume = 100
        elif volume < 0:
            self.volume = 0
        else:
            self.volume = volume

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1

    def mostrarVolume(self):
        return self.volume