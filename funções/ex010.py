'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados,
obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou.
Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira
jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os
dados até tirar este número novamente. Você perde, no entanto, se tirar um 7 antes de tirar este Ponto
novamente.
'''
from random import randint
from time import sleep


def craps(n1, n2, cont, ponto=0):
    s = n1 + n2
    if cont == 1:
        if s == 7 or s == 11:
            return 1
        elif s == 2 or s == 3 or s == 12:
            return 0
        else:
            ponto = s
            return ponto
    else:
        if s == ponto:
            return 1
        elif s == 7:
            return 0
        else:
            return 2


if __name__ == '__main__':
    contador = 1
    while True:
        n1 = randint(1, 6)
        print(f'Você tirou {n1} na primeira jogada')
        sleep(0.5)
        n2 = randint(1, 6)
        print(f'Você tirou {n2} na segunda jogada')
        sleep(0.5)
        print(f'A soma é {n1 + n2}')
        sleep(0.5)
        if contador == 1:
            if craps(n1, n2, contador) == 1:
                print('VOCÊ VENCEU!!!')
                break
            elif craps(n1, n2, contador) == 0:
                print('VOCÊ FEZ UM CRAPS E PERDEU!!!')
                break
            else:
                p = craps(n1, n2, contador)
                print(f'Seu ponto é {p}')
        else:
            if craps(n1, n2, contador, p) == 1:
                print('VOCÊ VENCEU!!!')
                break
            elif craps(n1, n2, contador, p) == 0:
                print('VOCÊ PERDEU!!!')
                break
            else:
                print('JOGUE NOVAMENTE!')
        contador += 1
        print('-' * 30)
