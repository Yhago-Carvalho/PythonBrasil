'''
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
'''

def imprime_numeros(num):
    for i in range(1, num + 1):
        for j in range(i):
            if i < 10:
                print(i, end='  ')
            else:
                print(i, end=' ')
        print()


if __name__ == '__main__':
    while True:
        try:
            n = int(input('Digite um número: '))
        except:
            print('tente novamente!')
        else:
            break
    imprime_numeros(n)
